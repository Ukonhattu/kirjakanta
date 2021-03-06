from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class UserForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=2, max=16)])
    password = PasswordField("Password", [validators.Length(min=2, max=16)])

    class Meta:
        csrf = False

class ModifyForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=2, max=16)], default="username")
    password = PasswordField("Password", [validators.Length(min=2, max=16)])


    class Meta:
        csrf = False
