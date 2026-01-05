from collections import namedtuple

from app.configuration.extension import db
from app.model.entity.portfolio import Portfolio
from sqlalchemy import text


def save_action(data):
    db.session.add(data)
    db.session.commit()

def get_user_portfolio(customer_id):
    sql = text("""
        SELECT *
        FROM portfolio p
        WHERE p.is_open = true
        AND p.customer_id = :customer_id
    """)

    result = db.session.execute(sql, {"customer_id": customer_id})

    out = []
    for r in result.mappings():
        out.append(
            Portfolio(
                ticker=r["ticker"],
                date=r["date"],
                price=r["price"],
                customer_id=r["customer_id"],
                qty=r["qty"],
                is_open=r["is_open"],
                action=r["action"],
            )
        )
    return out



def get_distinct_user_id():
    sql = text("""SELECT DISTINCT p.customer_id FROM portfolio p""")
    out = []
    try:
        result = db.session.execute(sql)
        Record = namedtuple('Record', result.keys())
        records = [Record(*r) for r in result.fetchall()]
        for r in records:
            res = r.customer_id
            out.append(res)
    except AttributeError:
        print("Attribute error")
    return out


def get_active_action(customer_id):
    sql = text("""
    SELECT *
    FROM portfolio p
    WHERE p.is_open = true
      AND p.action = 'BUY'
      AND p.customer_id = :customer_id
""")
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
    sql = text("""
    SELECT SUM(p.qty)
    FROM portfolio p
    WHERE p.ticker = :ticker
      AND p.is_open = true
      AND p.action = 'BUY'
      AND p.customer_id = :customer_id
""")
    result = db.session.execute(sql, {'ticker': ticker.ticker, 'customer_id': ticker.customer_id})
    Record = namedtuple('Record', result.keys())
    records = [Record(*r) for r in result.fetchall()]
    res = None
    for r in records:
        res = r.sum
    return res


def close_open_position(ticker):
    sql = text("""
    UPDATE portfolio
    SET is_open = false
    WHERE ticker = :ticker
      AND is_open = true
      AND action = 'BUY'
""")
    result = db.session.execute(sql, {'ticker': ticker})
