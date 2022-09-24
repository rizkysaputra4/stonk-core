from collections import namedtuple

from app.configuration.extension import db
from app.model.entity.ticker import Ticker


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


def get_lq45_ticker():
    sql = "select t.* from tickers l " \
          "left join tickers t on l.ticker = t.ticker"
    result = db.session.execute(sql)
    Record = namedtuple('Record', result.keys())
    records = [Record(*r) for r in result.fetchall()]
    tickers = []
    for r in records:
        ticker = Ticker(ticker=r.ticker, name=r.name, ipo_date=r.ipo_date, total_stock=r.total_stock)
        tickers.append(ticker)
    return tickers
