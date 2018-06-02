from flask import Flask
from flask_cors import CORS

from .api import register_api
from .auth import create_auth
from .config import flask_config


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "*"}}, supports_credentials=True)
    app.config.from_object(flask_config)

    create_auth(app)

    register_api(app)

    return app
