from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, HiddenField
from wtforms_components import read_only
from wtforms.validators import DataRequired, Length


class YoutubeDownloadForm(FlaskForm):
    url = StringField('Video URL', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Download Video')

