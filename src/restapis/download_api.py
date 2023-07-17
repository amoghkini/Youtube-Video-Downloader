from flask import flash, g, redirect, render_template, url_for
from flask.views import MethodView

from forms.youtube_download_form import YoutubeDownloadForm
from pytube import YouTube

class DownloadAPI(MethodView):
    
    def post(self):
        try:
            if not g.user:
                return render_template('index.html')

            form = YoutubeDownloadForm()

            download_url: str = form.url.data
            youtube_video = YouTube(download_url)
            youtube_video.register_on_progress_callback(on_download_process)

            print("Title: ", youtube_video.title)
            print("No of views: ", youtube_video.views)
            print("Description: ", youtube_video.description)

            stream = youtube_video.streams.get_highest_resolution()
            print("Loading...")

            stream.download()
            print("Ok")
            flash("Video downloaded successfully!!!", 'success')
            return redirect(url_for('home_api'))

        except Exception as e:
            flash(str(e), 'danger')
            return render_template('home.html', form=form)


def on_download_process(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percentage = bytes_downloaded * 100 / stream.filesize

    print(f"Downloading...{int(percentage)}")
