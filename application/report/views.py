from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.report.models import Report
from application.naturesites.models import NatureSite
from application.report.forms import NewReportForm
from application.auth.models import User

@app.route("/naturesites/edit/<naturesite_id>/report/new/", methods=["GET"])
@login_required
def report_createform(naturesite_id):
    t = NatureSite.query.get(naturesite_id)
    return render_template("report/newreport.html", form = NewReportForm(), naturesite=t)


@app.route("/naturesites/edit/<naturesite_id>/", methods=["POST", "GET"])
@login_required
def report_create(naturesite_id):
    form = NewReportForm(request.form)

    if not form.validate():
        return render_template("report/newreport.html", form = form)

    r = Report(form.title.data, form.description.data)
    r.account_id = current_user.id

    r.naturesite_id = naturesite_id

    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("naturesite_edit", naturesite_id=naturesite_id)) 

@app.route("/reports/", methods=["GET"])
def report_index():
    return render_template("report/list.html", reports = Report.allreports()) 


@app.route("/naturesites/edit/<naturesite_id>/changedis/<report_id>/", methods=["POST"])
@login_required
def report_change_description(naturesite_id, report_id):

    r = Report.query.get(report_id)
    r.description = request.form.get("description")
    db.session().commit()
  
    return redirect(url_for("naturesite_edit", naturesite_id=naturesite_id))


@app.route("/naturesites/edit/<naturesite_id>/delete/<report_id>/", methods=["POST"])
@login_required
def delete_report( naturesite_id, report_id):

    r = Report.query.get(report_id)

    db.session.delete(r)
    db.session().commit()
  
    return redirect(url_for("naturesite_edit", naturesite_id=naturesite_id))     


