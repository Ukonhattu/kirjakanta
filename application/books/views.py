from flask import render_template, request, redirect, url_for
from application import app, db
from application.books.models import Book


@app.route("/books", methods=["GET"])
def books_index():
    return render_template("books/list.html", books = Book.query.all())

@app.route("/books/new/")
def books_form():
    return render_template("books/new.html")

@app.route("/books/<book_id>/", methods=["POST"])
def book_set_read(book_id):
    book = Book.query.get(book_id)
    book.read = True
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/", methods=["POST"])
def books_create():
    name = Book(request.form.get("name"))

    db.session().add(name)
    db.session().commit()

    return redirect(url_for("books_index"))
