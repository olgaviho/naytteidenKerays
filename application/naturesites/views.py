from application import app, db
from flask import render_template, request
from application.naturesites.models import NatureSite

@app.route("/naturesites/new/")
def naturesites_form():
    return render_template("naturesites/new.html")

@app.route("/naturesites/", methods=["POST"])
def naturesites_create():
    n = NatureSite(request.form.get("name"))

    db.session().add(n)
    db.session().commit()
  
    return "hello world!"
