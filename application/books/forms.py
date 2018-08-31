from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class BookForm(FlaskForm):
    name  = StringField("Book name", [validators.Length(min=2, max=50)])
    genres = StringField("Genres", [validators.Length(min=2, max=120)])
    authors = StringField("Authors", [validators.Length(min=2, max=120)])
    series  = StringField("Serie", [validators.Length(min=0, max=50)])
    read = BooleanField("Read")

    class Meta:
        csrf = False
