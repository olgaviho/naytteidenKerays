from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.naturesites.models import NatureSite
from application.naturesites.forms import NatureSiteForm
from application.naturesites.forms import NatureSiteEditForm

@app.route("/naturesites", methods=["GET"])
def naturesites_index():
    return render_template("naturesites/list.html", naturesites = NatureSite.query.all())

@app.route("/naturesites/new/")
@login_required
def naturesites_form():
    return render_template("naturesites/new.html", form = NatureSiteForm())

@app.route("/naturesites/<naturesite_id>/", methods=["POST"])
@login_required
def naturesite_change_description(naturesite_id):

    t = NatureSite.query.get(naturesite_id)
    t.description = request.form.get("description")
    db.session().commit()
  
    return redirect(url_for("naturesites_index"))    

@app.route("/naturesites/", methods=["POST"])
@login_required
def naturesites_create():
    form = NatureSiteForm(request.form)

    if not form.validate():
        return render_template("naturesites/new.html", form = form)

    n = NatureSite(form.name.data, form.description.data)
    n.account_id = current_user.id

    db.session().add(n)
    db.session().commit()
  
    return redirect(url_for("naturesites_index"))

@app.route("/naturesites/edit/<naturesite_id>/", methods=["GET"])
@login_required
def naturesite_edit(naturesite_id):
    t = NatureSite.query.get(naturesite_id)
    return render_template("naturesites/edit.html",  form = NatureSiteEditForm(), naturesite=t)