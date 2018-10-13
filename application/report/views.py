from application import app, db, login_manager, login_required

from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.report.models import Report
from application.naturesites.models import NatureSite
from application.report.forms import NewReportForm
from application.auth.models import User
from application.report.forms import ReportEditForm

@app.route("/naturesites/edit/<naturesite_id>/report/", methods=["GET"])
@login_required(role="ADMIN")
def report_createform(naturesite_id):
    n = NatureSite.query.get(naturesite_id)
    
    if not n:
        return render_template("error.html",  message = "ERROR! Can't find Nature site")
    return render_template("report/newreport.html", form = NewReportForm(), naturesite=n)


@app.route("/naturesites/edit/<naturesite_id>/report/create/", methods=["POST"])
@login_required(role="ADMIN")
def report_create(naturesite_id):
   
    form = NewReportForm(request.form)
    n = NatureSite.query.get(naturesite_id)
    
    if not n:
        return render_template("error.html",  message = "ERROR! Can't find Nature site")

    if not form.validate():
        return render_template("report/newreport.html", form = form, naturesite = n)

    r = Report(form.title.data, form.description.data)
    r.account_id = current_user.id

    r.naturesite_id = naturesite_id

    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("naturesite_edit", naturesite_id=naturesite_id)) 

@app.route("/reports/", methods=["GET"])
def report_index():
    return render_template("report/list.html", reports = Report.allreports()) 

@app.route("/reports/edit/<report_id>/<naturesite_id>/", methods=["GET"])
@login_required(role="ADMIN")
def report_edit(report_id, naturesite_id):

    r = Report.query.get(report_id)
    
    if not r:
        return render_template("error.html",  message = "ERROR! Can't find Nature site")
    
    n = NatureSite.query.get(naturesite_id)
    
    if not n:
        return render_template("error.html",  message = "ERROR! Can't find Nature site")

    if r.account_id != current_user.id:
        return login_manager.unauthorized()
    
    return render_template("report/edit.html", form=ReportEditForm(), report_id = report_id, naturesite_id= naturesite_id )     


@app.route("/naturesites/edit/<report_id>/<naturesite_id>/description/", methods=["POST"])
@login_required(role="ADMIN")
def report_change_description(report_id, naturesite_id):

    r = Report.query.get(report_id)
    if not r:
        return render_template("error.html",  message = "ERROR! Can't find Nature site")
    n = NatureSite.query.get(naturesite_id)
    if not n:
        return render_template("error.html",  message = "ERROR! Can't find Nature site")

    if r.account_id != current_user.id:
        return login_manager.unauthorized()

    form = ReportEditForm(request.form)

    # joku menee pahasti tässä pieleen?
    if not form.validate():
        return render_template("report/edit.html", form = form, naturesite_id = n.id, report_id= r.id)  

    r.description = form.description.data
    db.session().commit()
  
    return redirect(url_for("naturesite_edit", naturesite_id=naturesite_id))


@app.route("/naturesites/edit/<report_id>/<naturesite_id>/delete", methods=["POST"])
@login_required(role="ADMIN")
def delete_report(report_id, naturesite_id):

    r = Report.query.get(report_id)
    if not r:
        return render_template("error.html",  message = "ERROR! Can't find Nature site")
    
    n = NatureSite.query.get(naturesite_id)
    if not n:
        return render_template("error.html",  message = "ERROR! Can't find Nature site")

    if r.account_id != current_user.id:
        return login_manager.unauthorized()

    db.session.delete(r)
    db.session().commit()
  
    return redirect(url_for("naturesite_edit", naturesite_id=naturesite_id))     



