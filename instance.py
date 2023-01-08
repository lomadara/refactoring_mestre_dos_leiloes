from flask import Flask, Blueprint
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix
from flask_restplus.apidoc import apidoc
from flask_cors import CORS
from os import environ

URL_PREFIX = '/teste'

class Server(object):
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.app.wsgi_app = ProxyFix(self.app.wsgi_app)
        apidoc.url_prefix = URL_PREFIX
        self.blueprint = Blueprint('api',__name__, url_prefix=URL_PREFIX)
        self.api = Api(
            doc='/docs',
            title="mestre_dos_leiloes",
            description="docs",
            version="2.0.0",
            contact="",
            default="mestre_dos_leiloes",
            default_label="mestre_dos_leiloes"
        )
        self.api.init_app(self.blueprint)
        self.health_check = self.health_check()
        self.app.register_blueprint(self.blueprint)
        
        CORS(self.app)
        
    def health_check(self):
        return self.api.namespace(
            name='Health check',
            description="",
            path="/healthcheck"
        )
        
    def run(self):
        self.app.run(
            debug=True,
            port=5000
        )

server = Server()

application = server.app

@application.before_request
def open_db_connection():
    pass

@application.teardown_appcontext
def close_db_connection(response):
    pass
