from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import CreateAccountForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())
  
    form = LoginForm(request.form)

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

@app.route("/auth/createform/")
def auth_form():
    return render_template("auth/registform.html", form2 = CreateAccountForm())

@app.route("/auth/create/", methods=["POST"])
def auth_create():
    form2 = CreateAccountForm(request.form)

    if not form2.validate():
        return render_template("auth/registform.html", form2 = form2)


    u = User(form2.name.data, form2.username.data, form2.password.data)

    sameuser = User.query.filter_by(username=form2.username.data).first()
    if sameuser:
        return render_template("auth/registform.html", form2 = form2,
                                error = "Username must be unique")

    db.session().add(u)
    db.session().commit()
  
    return redirect(url_for("naturesites_index"))
                               