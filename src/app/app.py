import os
from flask import Flask
from app.endpoints import register_endpoints


def create_app() -> Flask:
    app = _create_app()
    return app
    
    
def _create_app():
    app = Flask(__name__, template_folder=os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), 'templates'))
    register_endpoints(app)
    return app