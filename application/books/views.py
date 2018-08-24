from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.books.models import Book
from application.books.forms import BookForm
from application.genre.models import Genre
from application.author.models import Author


@app.route("/books", methods=["GET"])
@login_required()
def books_index():
    return render_template("books/list.html", books = Book.query.order_by("id").filter_by(account_id = current_user.id))

@app.route("/books/new/")
@login_required()
def books_form():
    return render_template("books/new.html", form=BookForm())

@app.route("/books/<book_id>/", methods=["POST"])
@login_required()
def book_set_read(book_id):

    b = Book.query.get(book_id)
    if b.read:
        b.read = False
    else:
        b.read = True
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/", methods=["POST"])
@login_required()
def books_create():
    form = BookForm(request.form)

    if not form.validate():
        return render_template("books/new.html", form = form)

    book = Book(form.name.data)
    book.read = form.read.data
    book.account_id = current_user.id

    genres = form.genres.data.split(";")

    for genre in genres:
        g = Genre.query.filter_by(name=genre).first()
        if g is not None:
            book.genres.append(g)
        else:
            g = Genre(genre)
            db.session.add(g)
            book.genres.append(g)
        db.session.commit()

    authors = form.authors.data.split(";")

    for author in authors:
        a = Author.query.filter_by(name=author).first()
        if a is not None:
            book.authors.append(a)
        else:
            a = Author(author)
            db.session.add(a)
            book.authors.append(a)
        db.session.commit()



    db.session().add(book)
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/delete/<book_id>/", methods=["POST"])
@login_required()
def books_delete(book_id):

    b = Book.query.get(book_id)
    if b.account_id != current_user.id:
        return login_manager.unauthorized()
    db.session().delete(b)
    db.session.commit()

    return redirect(url_for("books_index"))
