from flask_wtf import FLaskForm
from wtforms import StringField

class BookForm(FLaskForm):
    name StringField("Book name", validators.Length(min=2))
    read = BooleanField("Read")

    class Meta:
        csrf = False
