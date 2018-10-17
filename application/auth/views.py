from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from application import app, db, login_manager
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
    return render_template("auth/registform.html", accountform = CreateAccountForm())

@app.route("/auth/create/", methods=["POST"])
def auth_create():
    accountform = CreateAccountForm(request.form)

    if not accountform.validate():
        return render_template("auth/registform.html", accountform = accountform)


    password = accountform.password.data
    repeat_password = accountform.repeat_password.data    

    if password != repeat_password:
        return render_template("auth/registform.html", accountform = accountform,
                                error = "Passwords don't match")

    u = User(accountform.name.data, accountform.username.data, accountform.password.data)

    sameuser = User.query.filter_by(username=accountform.username.data).first()
    if sameuser:
        return render_template("auth/registform.html", accountform = accountform,
                                error = "Username must be unique")                            

    db.session().add(u)
    db.session().commit()
  
    return redirect(url_for("index"))
                               