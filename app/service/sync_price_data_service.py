from datetime import datetime, timedelta

import yfinance as yf

from app.configuration.extension import db
from app.model.entity.price import Price
from app.repository.price_repository import get_latest_data, delete_today_price
from app.repository.ticker_repository import get_all_ticker


def sync_price_data():
    tickers = get_all_ticker()
    delete_today_price()

    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)

    for company in tickers:
        print(company.ticker)

        price = get_latest_data(company.ticker)

        start = None
        period = None

        if price is None:
            period = "max"
        elif price.date < today:
            start = price.date + timedelta(days=1)
        else:
            continue

        raw_data = yf.download(
            company.ticker + ".JK",
            start=start.strftime("%Y-%m-%d") if start else None,
            end=tomorrow.strftime("%Y-%m-%d"),
            period=period,
            auto_adjust=False,
            progress=False,
            threads=False,
            )

        if raw_data.empty:
            continue

        for i, (date, row) in enumerate(raw_data.iterrows()):
            if price and price.date >= date.date():
                continue

            if row.isna().any():
                continue

            db.session.add(
                Price(
                    ticker=company.ticker,
                    date=date.to_pydatetime(),
                    open=float(row["Open"]),
                    high=float(row["High"]),
                    low=float(row["Low"]),
                    close=float(row["Close"]),
                    volume=int(row["Volume"]),
                    adj_close=float(row["Adj Close"]),
                )
            )

            if i % 100 == 0:
                db.session.commit()

        db.session.commit()


