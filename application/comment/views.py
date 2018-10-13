from application import app, db, login_manager, login_required

from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.report.models import Report
from application.naturesites.models import NatureSite
from application.comment.forms import NewCommentForm
from application.comment.forms import CommentEditForm
from application.auth.models import User
from application.comment.models import Comment


@app.route("/comment/<report_id>/<naturesite_id>", methods=["GET"])
@login_required(role="ADMIN")
def show_comments(report_id, naturesite_id):

    r = Report.query.get(report_id)
    if not r:
        return render_template("error.html",  message = "ERROR! Can't find report")
    n = NatureSite.query.get(naturesite_id)
    if not n:
        return render_template("error.html",  message = "ERROR! Can't find Nature site")

    return render_template("comment/index.html", form2=CommentEditForm(),form=NewCommentForm(), report = r, naturesite = n) 

@app.route("/comment/<report_id>/<naturesite_id>/newcomment/", methods=["POST"])
@login_required(role="ADMIN")
def comment_create(report_id, naturesite_id,):
    r = Report.query.get(report_id)
    if not r:
        return render_template("error.html",  message = "ERROR! Can't find report")
    n = NatureSite.query.get(naturesite_id)
    if not n:
        return render_template("error.html",  message = "ERROR! Can't find Nature site")

    form = NewCommentForm(request.form)
    
    if not form.validate():
        return render_template("comment/index.html", form2=CommentEditForm(), form = form, report = r, naturesite=n)

    c = Comment(form.text.data)

    c.account_id = current_user.id
    c.report_id = report_id

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("show_comments", report_id = report_id, naturesite_id=naturesite_id)) 


@app.route("/comment/<report_id>/<naturesite_id>/changetext/<comment_id>/", methods=["POST"])
@login_required(role="ADMIN")
def comment_change_description(report_id, naturesite_id, comment_id):

    c = Comment.query.get(comment_id)
    if not c:
        return render_template("error.html",  message = "ERROR! Can't find comment")

    form2 = CommentEditForm(request.form)

    r = Report.query.get(report_id)
    if not r:
        return render_template("error.html",  message = "ERROR! Can't find Report")
    n = NatureSite.query.get(naturesite_id)
    if not n:
        return render_template("error.html",  message = "ERROR! Can't find Nature site")

    if c.account_id != current_user.id:
        return login_manager.unauthorized()
    
    # tässä jotain tapahtuu nyt...
    if not form2.validate():
        return render_template("comment/index.html", form2=form2, form = NewCommentForm(request.form), report = r, naturesite=n)    

    c.text = request.form.get("newtext")
    db.session().commit()
  
    return redirect(url_for("show_comments", report_id = report_id, naturesite_id=naturesite_id)) 


@app.route("/comment/<report_id>/<naturesite_id>/delete/<comment_id>/", methods=["POST"])
@login_required(role="ADMIN")
def delete_comment( report_id, naturesite_id, comment_id):

    c = Comment.query.get(comment_id)
    if not c:
        return render_template("error.html",  message = "ERROR! Can't find the Comment")
    r = Report.query.get(report_id)
    if not r:
        return render_template("error.html",  message = "ERROR! Can't find the Report")
    n = NatureSite.query.get(naturesite_id)
    if not n:
        return render_template("error.html",  message = "ERROR! Can't find the Nature site")

    if c.account_id != current_user.id:
        return login_manager.unauthorized()

    db.session.delete(c)
    db.session().commit()
  
    return redirect(url_for("show_comments", report_id = report_id, naturesite_id=naturesite_id))     

