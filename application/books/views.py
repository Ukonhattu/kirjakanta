from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.books.models import Book
from application.books.forms import BookForm


@app.route("/books", methods=["GET"])
@login_required
def books_index():
    return render_template("books/list.html", books = Book.query.filter_by(account_id = current_user.id))

@app.route("/books/new/")
@login_required
def books_form():
    return render_template("books/new.html", form=BookForm())

@app.route("/books/<book_id>/", methods=["POST"])
@login_required
def book_set_read(book_id):

    b = Book.query.get(book_id)
    b.read = True
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/", methods=["POST"])
@login_required
def books_create():
    form = BookForm(request.form)

    if not form.validate():
        return render_template("books/new.html", form = form)

    book = Book(form.name.data)
    book.read = form.read.data
    book.account_id = current_user.id

    db.session().add(book)
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/delete/<book_id>/", methods=["POST"])
@login_required
def books_delete(book_id):

    b = Book.query.get(book_id)
    db.session().delete(b)
    db.session.commit()

    return redirect(url_for("books_index"))
