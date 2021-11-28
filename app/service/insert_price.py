import plotly.graph_objects as go
import pandas as pd
import yfinance as yf
from extension import db
from app.model.price import Price


def insertPrice(price: Price):

    stockPrice = Price()
    # db.session.add(price)
    # db.session.commit()
    msft = yf.Ticker("BMRI.JK")

    # get stock info
    msft.info
    hist = msft.history(period="max")
    data = pd.DataFrame(hist)
    print(data.columns.values)
    print(data)
