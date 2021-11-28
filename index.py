
from flask import Flask
from extension import db
from app.controller.price_info import price_info
from app.controller.yahoo_api import yahoo_api


def register_extensions(app):
    db.init_app(app)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/stonk'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.register_blueprint(price_info)
    app.register_blueprint(yahoo_api)

    register_extensions(app)
    print("running app...")

    return app


app = create_app()
app.run(port=8087, debug=True)
