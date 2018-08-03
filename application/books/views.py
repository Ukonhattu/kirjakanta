from flask import render_template, request
from application import app, db
from application.books.models import Book

@app.route("/books/new/")
def books_form():
    return render_template("books/new.html")

@app.route("/books/", methods=["POST"])
def books_create():
    name = Book(request.form.get("name"))

    db.session().add(name)
    db.session().commit()

    return "hello world"
