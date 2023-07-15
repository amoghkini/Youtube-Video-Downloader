import json
import logging
import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv('../.env')

APP_NAME = "Algo Trading Framework"
ALGO_NAME = "Algo Trader"
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TEMPLATE_FOLDER = os.path.join(PROJECT_ROOT, 'templates')
STATIC_FOLDER = os.path.join(PROJECT_ROOT, 'static')

def get_server_config():
    with open('../config/server.json', 'r') as server:
        json_server_data = json.load(server)
        return json_server_data


def get_env():
    return get_server_config().get('env')


class BaseConfig(object):
    
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY','This is secret key')
    
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=get_server_config().get('sessionLifetime'))

class ProdConfig(BaseConfig):

    ENV = 'prod'
    DEBUG = True if get_env() == 'dev' else False

    # Database Credentials


class DevConfig(BaseConfig):
    ENV =  'dev'
    DEBUG = True if get_env() == 'dev' else False
    
class TestingConfig(BaseConfig):
    ENV = 'qa'
    DEBUG = True if get_env() == 'dev' else False
