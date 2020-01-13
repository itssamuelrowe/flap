
import os
from flask import Flask
from configuration import configuration

def create_app(config_name='default'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configuration[config_name])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
