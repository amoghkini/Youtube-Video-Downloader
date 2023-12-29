from flask import render_template, g
from flask.views import MethodView


class HomeAPI(MethodView):
    
    def get(self):
        if g.user:
            return render_template('home.html', form={})
        return render_template('index.html')