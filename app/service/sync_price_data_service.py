from datetime import datetime, timedelta

import yfinance as yf

from app.configuration.extension import db
from app.model.entity.price import Price
from app.repository.price_repository import get_latest_data, delete_today_price
from app.repository.ticker_repository import get_all_ticker


def sync_price_data():
    tickers = get_all_ticker()
    delete_today_price()
    for company in tickers:
        print(company.ticker)
        price = get_latest_data(company.ticker)
        period = None
        string_last_date = None
        if price is None:
            period = 'max'
        elif price.date is not None and price.date < datetime.now().date():
            string_last_date = (price.date + timedelta(days=1)).strftime('%Y-%m-%d')
        else:
            continue

        string_current_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        raw_data = yf.download(company.ticker + '.JK', period=period, start=string_last_date, end=string_current_date)
        print(raw_data.tail(2))
        for index, (date, row) in enumerate(raw_data.iterrows()):
            if price is not None and price.date >= date:
                continue
            stock_price = Price(
                ticker=company.ticker,
                date=date,
                open=row['Open'],
                high=row['High'],
                low=row['Low'],
                close=row['Close'],
                volume=row['Volume'],
                adj_close=row['Adj Close']
            )
            db.session.add(stock_price)
            if index is len(raw_data) - 1 or index % 100 == 0:
                db.session.commit()
        db.session.commit()
