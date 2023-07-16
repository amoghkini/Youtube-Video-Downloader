from flask import flash, redirect, url_for, session
from flask.views import MethodView

class LogOutAPI(MethodView):

    def get(self):
        session.pop('user',None)
        return redirect(url_for('home_api'))
