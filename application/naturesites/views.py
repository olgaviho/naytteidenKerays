from application import app, db, login_manager

from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

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
   

@app.route("/naturesites/", methods=["POST"])
@login_required
def naturesites_create():

    form = NatureSiteForm(request.form)


    if not form.validate():
        return render_template("naturesites/new.html", form = form)

    n = NatureSite(form.name.data, form.description.data)

    samenaturesite = NatureSite.query.filter_by(name=form.name.data).first()

    if samenaturesite:
        return render_template("naturesites/new.html", form = form, error = "Name must be unique") 


    n.account_id = current_user.id

    db.session().add(n)
    db.session().commit()
  
    return redirect(url_for("naturesites_index"))

@app.route("/naturesites/show/<naturesite_id>", methods=["GET"])
@login_required
def naturesite_show(naturesite_id):

    n = NatureSite.query.get(naturesite_id)

    if not n:
        return render_template("error.html",  message = "ERROR! Can't find the Nature site")

    return render_template("naturesites/show.html", naturesite=n, id = current_user.id)

@app.route("/naturesites/show/<naturesite_id>/edit/", methods=["GET"])
@login_required
def naturesite_edit(naturesite_id):
 
    n = NatureSite.query.get(naturesite_id)
    
    if not n:
        return render_template("error.html",  message = "ERROR! Can't find the Nature site")


    if n.account_id != current_user.id:
        return login_manager.unauthorized()
    
    return render_template("naturesites/edit.html", form = NatureSiteEditForm(), naturesite = n)   

@app.route("/naturesites/show/<naturesite_id>/edit/change/", methods=["POST"])
@login_required
def naturesite_change_description(naturesite_id):

    n = NatureSite.query.get(naturesite_id)
    
    if not n:
        return render_template("error.html",  message = "ERROR! Can't find the Nature site")

    if n.account_id != current_user.id:
        return login_manager.unauthorized()

    form = NatureSiteEditForm(request.form)

    if not form.validate():
        return render_template("naturesites/edit.html", form = form, naturesite = n)

    n.description = form.description.data
    db.session().commit()
  
    return redirect(url_for("naturesite_show", naturesite_id = naturesite_id)) 

