from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, UserForm, ModifyForm
from application.books.models import Book

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/")
def user_form():
    return render_template("auth/new.html", form=UserForm())


@app.route("/auth/", methods=["POST"])
def user_create():
    form = UserForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    user = User(form.username.data, form.username.data, form.password.data)


    db.session().add(user)
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/auth/userpage/modify", methods=["POST"])
@login_required()
def user_modify():
    form = UserForm(request.form)

    if not form.validate():
        return render_template("auth/userpage.html", form = form)
    current_user.username = form.username.data
    current_user.password = form.password.data
    current_user.name = form.username.data

    db.session.commit()

    return redirect(url_for("user_page"))

@app.route("/auth/userpage")
@login_required()
def user_page():
    form = ModifyForm()
    form.username.default = current_user.username
    form.process()
    return render_template("auth/userpage.html", form = form)

@app.route("/auth/userpage/delete", methods=["POST"])
@login_required()
def user_delete():
    book = Book.query.filter_by(account_id=current_user.id).all()
    for b in book:
        db.session.delete(b)
    db.session.delete(current_user)
    db.session.commit()
    logout_user()

    return redirect(url_for("books_index"))
