from extension import db


class Price(db.Model):
    ticker = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    open = db.Column(db.Numeric, nullable=False)
    close = db.Column(db.Numeric, nullable=False)
    high = db.Column(db.Numeric, nullable=False)
    low = db.Column(db.Numeric, nullable=False)
    volume = db.Column(db.BigInteger)
    divident = db.Column(db.Numeric)
    stock_split = db.Column(db.Numeric)

    def __init__(self,
                 ticker,
                 date,
                 open,
                 close,
                 high,
                 low,
                 volume,
                 divident,
                 stock_split,):
        self.ticker = ticker
        self.date = date
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume
        self.divident = divident
        self.stock_split = stock_split

    __mapper_args__ = {
        "primary_key": [ticker, date]
    }
