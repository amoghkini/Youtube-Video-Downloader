from flask import render_template
from flask.views import MethodView


class HomeAPI(MethodView):

    def get(self):
        
        return render_template('home.html')
