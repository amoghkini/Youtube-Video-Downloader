from flask import render_template, g
from flask.views import MethodView

from forms.youtube_download_form import YoutubeDownloadForm

class HomeAPI(MethodView):
    
    def get(self):
        if g.user:
            form = YoutubeDownloadForm()
            return render_template('home.html', form=form)
        return render_template('index.html')