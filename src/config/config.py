import json
import os
from datetime import timedelta
from dotenv import load_dotenv
from typing import Dict

from common.execution_env import ExecutionEnv

APP_NAME: str = "Youtube Video Downloader"
PROJECT_ROOT: str = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
TEMPLATE_FOLDER: str = os.path.join(PROJECT_ROOT, 'src', 'templates')
STATIC_FOLDER: str = os.path.join(PROJECT_ROOT, 'src', 'static')
CONFIG_FOLDER: str = os.path.join(PROJECT_ROOT, 'config')

load_dotenv(os.path.join(os.pardir, '.env'))

def get_server_config() -> Dict:
    with open(os.path.join(CONFIG_FOLDER, 'server.json'), 'r') as server:
        return json.load(server)


def get_env() -> str:
    return get_server_config().get('env')


class BaseConfig(object):

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY','This is secret key')
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=get_server_config().get('sessionLifetime'))



class ProdConfig(BaseConfig):

    ENV = 'prod'
    DEBUG = get_env() == ExecutionEnv.PROD


class TestingConfig(BaseConfig):
    ENV = 'qa'
    DEBUG = get_env() == ExecutionEnv.TEST


class DevConfig(BaseConfig):
    ENV =  'dev'
    DEBUG = get_env() == ExecutionEnv.DEV