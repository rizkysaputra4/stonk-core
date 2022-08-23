import flask
from flask import Blueprint

from app.model.response.sync_data_response import BaseResponse
from app.service.get_recommendation_service import get_recommendation
from app.service.sync_price_data_service import sync_price_data

sync_price = Blueprint('yahoo_api', __name__)


@sync_price.route("/sync-data", methods=["GET"])
def sync_data_route():
    sync_price_data()
    resp = flask.Response(BaseResponse(data="Success").toJSON())
    resp.headers["Content-Type"] = "application/json"
    return resp


@sync_price.route("/today-pick", methods=["GET"])
def get_today_pick():
    data = get_recommendation()
    resp = flask.Response(BaseResponse(data=data).toJSON())
    resp.headers["Content-Type"] = "application/json"
    return resp
