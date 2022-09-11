from collections import namedtuple

import pandas as pd

from app.configuration.extension import db
from app.model.entity.price import Price


def get_latest_data(ticker):
    sql = "select * from price p where p.ticker = :ticker order by p.date desc limit 1"
    result = db.session.execute(sql, {'ticker': ticker})
    Record = namedtuple('Record', result.keys())
    records = [Record(*r) for r in result.fetchall()]

    res = None
    for r in records:
        res = Price(ticker=r.ticker, date=r.date, open=r.open, close=r.close,
                    high=r.high, low=r.low, volume=r.volume, adj_close=r.adj_close)
    return res


def get_price_history(ticker, since):
    sql = "select * from price p where ticker = '" + ticker + "' and p.date >= '" + since + "'::date order by p.date asc;"
    df = pd.read_sql(sql, db.session.bind)
    return df


def check_if_ticker_exist(ticker):
    sql = "SELECT COUNT(*) as total FROM price p " \
          "WHERE p.ticker = :ticker "
    result = db.session.execute(sql, {'ticker': ticker})
    Record = namedtuple('Record', result.keys())
    records = [Record(*r) for r in result.fetchall()]
    res = None
    for r in records:
        res = r.total
    return res


def delete_today_price():
    sql = "DELETE FROM price p WHERE p.date = current_date"
    db.session.execute(sql)


def save_all_price_data():
    print("save")
