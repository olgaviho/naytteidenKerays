from application import app, db, login_required, login_manager

from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.naturesites.models import NatureSite
from application.naturesites.forms import NatureSiteForm
from application.naturesites.forms import NatureSiteEditForm


@app.route("/naturesites", methods=["GET"])
def naturesites_index():
    return render_template("naturesites/list.html", naturesites = NatureSite.query.all())

@app.route("/naturesites/new/")
@login_required(role="ADMIN")
def naturesites_form():
    return render_template("naturesites/new.html", form = NatureSiteForm())

@app.route("/naturesites/<naturesite_id>/", methods=["POST"])
@login_required(role="ADMIN")
def naturesite_change_description(naturesite_id):

    t = NatureSite.query.get(naturesite_id)
    
    if not t:
        return render_template("error.html",  message = "ERROR! Can't find Nature site")

    if t.account_id != current_user.id:
        return login_manager.unauthorized()

    form = NatureSiteEditForm(request.form)

    if not form.validate():
        return render_template("naturesites/edit.html", form = form, naturesite = t)

    t.description = form.description.data
    db.session().commit()
  
    return redirect(url_for("naturesites_index"))    

@app.route("/naturesites/", methods=["POST"])
@login_required(role="ADMIN")
def naturesites_create():

    form = NatureSiteForm(request.form)

    if not form.validate():
        return render_template("naturesites/new.html", form = form)

    n = NatureSite(form.name.data, form.description.data)
    n.account_id = current_user.id

    db.session().add(n)
    db.session().commit()
  
    return redirect(url_for("naturesites_index"))

@app.route("/naturesites/edit/<naturesite_id>", methods=["GET"])
@login_required(role="ANY")
def naturesite_edit(naturesite_id):

    t = NatureSite.query.get(naturesite_id)
    if not t:
        return render_template("error.html",  message = "ERROR! Can't find Nature site")

    return render_template("naturesites/edit.html",  form = NatureSiteEditForm(), naturesite=t)
