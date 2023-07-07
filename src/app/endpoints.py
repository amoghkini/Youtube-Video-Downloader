from flask import Flask
from restapis import (home_api)


def register_endpoints(app: Flask)-> None:
    app.add_url_rule("/", view_func=home_api.HomeAPI.as_view("home_api"))