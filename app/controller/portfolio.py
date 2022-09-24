import flask
from flask import Blueprint, request

from app.model.entity.portfolio import Portfolio
from app.model.response.sync_data_response import BaseResponse
from app.service.portfolio_action import buy_service, sell_service, recap_service, get_user_portfolio_service

portfolio = Blueprint('portfolio', __name__)


@portfolio.route("/buy", methods=["POST"])
def buy():
    req = Portfolio(
        ticker=request.get_json().get('ticker'),
        price=request.get_json().get('price'),
        qty=request.get_json().get('qty'),
        action='BUY',
        customer_id=request.get_json().get('customerId')
    )

    result = buy_service(req)
    resp = flask.Response(BaseResponse(data=result).toJSON())
    resp.headers["Content-Type"] = "application/json"
    return resp


@portfolio.route("/sell", methods=["POST"])
def sell():
    req = Portfolio(
        ticker=request.get_json().get('ticker'),
        price=request.get_json().get('price'),
        qty=request.get_json().get('qty'),
        action='SELL',
        is_open=False,
        customer_id=request.get_json().get('customerId')
    )
    result = sell_service(req)
    resp = flask.Response(BaseResponse(data=result).toJSON())
    resp.headers["Content-Type"] = "application/json"
    return resp


@portfolio.route("/recap", methods=["POST"])
def analyze():
    out = recap_service(request.get_json().get('customerId'))
    resp = flask.Response(BaseResponse(data=out).toJSON())
    resp.headers["Content-Type"] = "application/json"
    return resp


@portfolio.route("/portfolio", methods=["GET"])
def get_portfolio():
    out = get_user_portfolio_service(request.get_json().get('customerId'))
    resp = flask.Response(BaseResponse(data=out).toJSON())
    resp.headers["Content-Type"] = "application/json"
    return resp
