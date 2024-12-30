import os

from flask import Flask

def create_app():
    # create and configure application
    app = Flask(__name__, instance_relative_config=True)

    # register blueprint
    from . import routes
    app.register_blueprint(routes.bp)

    return app