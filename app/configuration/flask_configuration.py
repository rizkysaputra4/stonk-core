import logging
import os

from flask import Flask

from app.configuration.extension import db
from app.controller.portfolio import portfolio
from app.controller.price_info import price_info
from app.controller.sync_price import sync_price


def register_extensions(app):
    db.app = app
    db.init_app(app)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.register_blueprint(price_info)
    app.register_blueprint(sync_price)
    app.register_blueprint(portfolio)
    # init_log_config()
    register_extensions(app)
    logging.info("App created")
    return app