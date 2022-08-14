import flask
from flask import Blueprint

from app.model.response.sync_data_response import BaseResponse
from app.service.sync_price_data import sync_price_data

yahoo_api = Blueprint('yahoo_api', __name__)

@yahoo_api.route("/sync-data", methods=["GET"])
def sync_data_route():
    sync_price_data()
    resp = flask.Response(BaseResponse(data="Success").toJSON())
    resp.headers["Content-Type"] = "application/json"
    return resp
