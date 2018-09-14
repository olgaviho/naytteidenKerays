from application import app, db
from flask import redirect, render_template, request, url_for
from application.naturesites.models import NatureSite

@app.route("/naturesites", methods=["GET"])
def naturesites_index():
    return render_template("naturesites/list.html", naturesites = NatureSite.query.all())

@app.route("/naturesites/new/")
def naturesites_form():
    return render_template("naturesites/new.html")

@app.route("/naturesites/<naturesite_id>/", methods=["POST"])
def naturesite_change_description(naturesite_id):

    t = NatureSite.query.get(naturesite_id)
    t.description = request.form.get("newdescription")
    db.session().commit()
  
    return redirect(url_for("naturesites_index"))    

@app.route("/naturesites/", methods=["POST"])
def naturesites_create():
    n = NatureSite(request.form.get("name"),request.form.get("description"))

    db.session().add(n)
    db.session().commit()
  
    return redirect(url_for("naturesites_index"))
