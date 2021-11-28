from datetime import datetime
from flask import Blueprint, render_template, session, abort
from app.model.price import Price

from app.service.insert_price import insertPrice

yahoo_api = Blueprint('yahoo_api', __name__)


@yahoo_api.route("/sync-data", methods=["GET"])
def hello():
    priceD = Price("INDF",
                   datetime.now(), 50000, 50000,
                   5000, 5000, 5000, 0, 0)
    insertPrice(priceD)
    return '<h2>test-success<h2>'
