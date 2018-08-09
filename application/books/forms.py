from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class BookForm(FlaskForm):
    name  = StringField("Book name", [validators.Length(min=2)])
    read = BooleanField("Read")

    class Meta:
        csrf = False
