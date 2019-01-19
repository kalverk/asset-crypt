from flask import Flask

from .api.decrypt import decrypt
from .api.encrypt import encrypt
from .config import app_config


def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])

    app.register_blueprint(encrypt)
    app.register_blueprint(decrypt)

    @app.route('/', methods=['GET'])
    def index():
        return 'Congratulations! Your first endpoint is workin'

    return app
