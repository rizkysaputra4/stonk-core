import flask
from flask import Blueprint

from app.model.response.sync_data_response import BaseResponse
from app.service.get_recommendation_service import get_recommendation

sync_price = Blueprint('yahoo_api', __name__)


@sync_price.route("/today-pick", methods=["GET"])
def get_today_pick():
    data = get_recommendation()
    resp = flask.Response(BaseResponse(data=data).toJSON())
    resp.headers["Content-Type"] = "application/json"
    return resp
