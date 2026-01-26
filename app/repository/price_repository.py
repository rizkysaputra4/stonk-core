from collections import namedtuple

import pandas as pd

from app.configuration.extension import db
from app.model.entity.price import Price
from sqlalchemy import text


def get_latest_data(ticker):
    sql = text("""
    SELECT *
    FROM price p
    WHERE p.ticker = :ticker
    ORDER BY p.date DESC
    LIMIT 1
""")
    result = db.session.execute(sql, {'ticker': ticker})
    Record = namedtuple('Record', result.keys())
    records = [Record(*r) for r in result.fetchall()]

    res = None
    for r in records:
        res = Price(ticker=r.ticker, date=r.date, open=r.open, close=r.close,
                    high=r.high, low=r.low, volume=r.volume, adj_close=r.adj_close)
    return res


def get_price_history(ticker, since):
    sql = """
        SELECT *
        FROM price p
        WHERE p.ticker = %(ticker)s
          AND p.date >= %(since)s::date
        ORDER BY p.date ASC
    """
    df = pd.read_sql(
        sql,
        db.engine,   # ✅ NOT db.session.bind
        params={"ticker": ticker, "since": since}
    )
    return df



def check_if_ticker_exist(ticker):
    sql = text("""
    SELECT COUNT(*) AS total
    FROM price p
    WHERE p.ticker = :ticker
""")
    result = db.session.execute(sql, {'ticker': ticker})
    Record = namedtuple('Record', result.keys())
    records = [Record(*r) for r in result.fetchall()]
    res = None
    for r in records:
        res = r.total
    return res


def delete_today_price():
    sql = text("""
    DELETE FROM price
    WHERE date = current_date
""")
    db.session.execute(sql)


def save_all_price_data():
    print("save")
