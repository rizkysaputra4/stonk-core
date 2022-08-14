import os

from flask import Flask

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

    register_extensions(app)
    print("running app...")
    return app


app = create_app()
run_job()
app.run(port=8087, debug=True)
