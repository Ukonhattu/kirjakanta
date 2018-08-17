from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class BookForm(FlaskForm):
    name  = StringField("Book name", [validators.Length(min=2, max=16)])
    genres = StringField("Genres", [validators.Length(min=2, max=10)])
    read = BooleanField("Read")

    class Meta:
        csrf = False
