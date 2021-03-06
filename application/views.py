from flask import render_template
from application import app
from application.auth.models import User

@app.route("/")
def index():
    return render_template("index.html", most_read=User.find_users_with_most_read_books())
