from flask import Blueprint

price_info = Blueprint('price_info', __name__)


@price_info.route("/world")
def world():
    return "Hello World from app 2!"
