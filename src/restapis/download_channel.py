from flask import g, render_template
from flask.views import MethodView

from forms.youtube_download_form import YoutubeDownloadForm


class DownloadChannelAPI(MethodView):

    def get(self):
        if g.user:
            form = YoutubeDownloadForm()
            return render_template('download_channel.html', form=form)
        return render_template('index.html')