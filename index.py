import os
import logging
from flask import Flask

from app.configuration.logger_configuration import init_log_config
from app.controller.price_info import price_info
from app.controller.sync_price import yahoo_api
from app.scheduler.schedule_job import run_job
from extension import db


def register_extensions(app):
    db.app = app
    db.init_app(app)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.register_blueprint(price_info)
    app.register_blueprint(yahoo_api)
    # init_log_config()
    register_extensions(app)
    logging.info("App created")
    return app


app = create_app()
run_job()
app.run(port=8087, debug=True)
