from collections import namedtuple

from app.model.entity.portfolio import Portfolio
from extension import db


def save_action(data):
    db.session.add(data)
    db.session.commit()


def get_active_action(customer_id):
    sql = "SELECT * FROM portfolio  p " \
          "WHERE p.is_open " \
          "AND p.action = 'BUY' " \
          "AND p.customer_id = :customer_id"
    out = []
    try:
        result = db.session.execute(sql, {'customer_id': customer_id})
        Record = namedtuple('Record', result.keys())
        records = [Record(*r) for r in result.fetchall()]
        for r in records:
            res = Portfolio(ticker=r.ticker, date=r.date, price=r.price, customer_id=r.customer_id,
                            qty=r.qty, is_open=r.is_open, action=r.action)
            out.append(res)
    except AttributeError:
        print("Attribute error")
    return out


def get_total_lot(ticker):
    sql = "SELECT SUM(p.qty) FROM portfolio  p " \
          "WHERE p.ticker = :ticker " \
          "AND p.is_open " \
          "AND p.action = 'BUY' " \
          "AND p.customer_id = :customer_id"
    result = db.session.execute(sql, {'ticker': ticker.ticker, 'customer_id': ticker.customer_id})
    Record = namedtuple('Record', result.keys())
    records = [Record(*r) for r in result.fetchall()]
    res = None
    for r in records:
        res = r.sum
    return res


def close_open_position(ticker):
    sql = "update portfolio set is_open = false " \
          "where ticker = :ticker " \
          "and is_open = true and action = 'BUY'"
    result = db.session.execute(sql, {'ticker': ticker})
