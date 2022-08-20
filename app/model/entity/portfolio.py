from datetime import datetime

from extension import db


class Portfolio(db.Model):
    __tablename__ = 'portfolio'

    # id = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Numeric, nullable=False, primary_key=True)
    ticker = db.Column(db.String, nullable=False)
    action = db.Column(db.String, nullable=False)
    qty = db.Column(db.Numeric, nullable=False)
    date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    is_open = db.Column(db.Boolean, nullable=False)

    def __init__(self,
                 ticker,
                 action,
                 price,
                 qty,
                 customer_id,
                 is_open = True,
                 date = datetime.now()):
        self.customer_id = customer_id
        self.ticker = ticker
        self.action = action
        self.date = date
        self.price = price
        self.qty = qty
        self.is_open = is_open


    # def __repr__(self):
    #     return f"buy date:{self.buy}, sell date:{self.sell}>"
    #
    # def __str__(self):
    #     return f"buy date {self.buy}, sell date {self.sell}"
