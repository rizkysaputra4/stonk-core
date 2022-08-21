from app.configuration.extension import db


class Price(db.Model):
    __tablename__ = 'price'

    ticker = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    open = db.Column(db.Numeric, nullable=False)
    close = db.Column(db.Numeric, nullable=False)
    high = db.Column(db.Numeric, nullable=False)
    low = db.Column(db.Numeric, nullable=False)
    volume = db.Column(db.BigInteger)
    adj_close = db.Column(db.Numeric)

    def __init__(self,
                 ticker,
                 date,
                 open,
                 close,
                 high,
                 low,
                 volume,
                 adj_close):
        self.ticker = ticker
        self.date = date
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume
        self.adj_close = adj_close

    __mapper_args__ = {
        "primary_key": [ticker, date]
    }
