from flask import Flask
from sample_app.config import Config

def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(Config)

    from sample_app.main.routes import main
    from sample_app.errors.handlers import errors

    application.register_blueprint(main)
    application.register_blueprint(errors)

    return application