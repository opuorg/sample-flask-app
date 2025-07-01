from flask import Flask
from sample_app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from sample_app.main.routes import main
    from sample_app.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app