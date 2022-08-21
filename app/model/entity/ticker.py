from app.configuration.extension import db


class Ticker(db.Model):
    ticker = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    ipo_date = db.Column(db.Date, nullable=False)
    total_stock = db.Column(db.Integer, nullable=False)

    def __init__(self, ticker, name, ipo_date, total_stock, ):
        self.ticker = ticker
        self.name = name
        self.ipo_date = ipo_date
        self.total_stock = total_stock

    __mapper_args__ = {
        "primary_key": [ticker]
    }