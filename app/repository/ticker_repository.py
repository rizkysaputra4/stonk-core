from collections import namedtuple

from app.model.entity.ticker import Ticker
from extension import db


def get_all_ticker():
    try:
        result = db.session.execute("SELECT * FROM tickers")
        Record = namedtuple('Record', result.keys())
        records = [Record(*r) for r in result.fetchall()]
        tickers = []
        for r in records:
            ticker = Ticker(ticker=r.ticker, name=r.name, ipo_date=r.ipo_date, total_stock=r.total_stock)
            tickers.append(ticker)
        return tickers
    except AttributeError:
        print("Attribute error")

