from application import app, db, login_manager

from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from application.report.models import Report
from application.naturesites.models import NatureSite
from application.comment.forms import NewCommentForm
from application.comment.forms import CommentEditForm
from application.auth.models import User
from application.comment.models import Comment

@app.route("/comment", methods=["GET"])
@login_required
def s():

    return render_template("comment/index.html") 

@app.route("/comment/<report_id>/<naturesite_id>", methods=["GET"])
@login_required
def show_comments(report_id, naturesite_id):

    r = Report.query.get(report_id)

    if not r:
        return render_template("error.html",  message = "ERROR! Report not found")  
    
    n = NatureSite.query.get(naturesite_id)
    
    if not n:
        return render_template("error.html",  message = "ERROR! Nature site not found")

    return render_template("comment/index.html", form=NewCommentForm(), report = Report.query.get(report_id), naturesite = NatureSite.query.get(naturesite_id), id = current_user.id) 

@app.route("/comment/<report_id>/<naturesite_id>/newcomment/", methods=["POST"])
@login_required
def comment_create(report_id, naturesite_id,):

    r = Report.query.get(report_id)

    if not r:
        return render_template("error.html",  message = "ERROR! Report not found")  
    
    n = NatureSite.query.get(naturesite_id)
    
    if not n:
        return render_template("error.html",  message = "ERROR! Nature site not found")


    form = NewCommentForm(request.form)
    
    if not form.validate():
        return render_template("comment/index.html", form = form, report = Report.query.get(report_id), naturesite=NatureSite.query.get(naturesite_id))

    c = Comment(form.text.data)

    c.account_id = current_user.id
    c.report_id = report_id

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("show_comments", report_id = report_id, naturesite_id=naturesite_id)) 


@app.route("/comment/<report_id>/<naturesite_id>/<comment_id>/changetext/", methods=["POST"])
@login_required
def comment_change_description(report_id, naturesite_id, comment_id):

    r = Report.query.get(report_id)

    if not r:
        return render_template("error.html",  message = "ERROR! Report not found")  
    
    n = NatureSite.query.get(naturesite_id)
    
    if not n:
        return render_template("error.html",  message = "ERROR! Nature site not found")
    
    c = Comment.query.get(comment_id)

    if not c:
        return render_template("error.html",  message = "ERROR! Comment not found")

    form = CommentEditForm(request.form)

    if c.account_id != current_user.id:
        return login_manager.unauthorized()
    
    if not form.validate():
        return render_template("comment/edit.html", form=form, report = report_id, naturesite_id = naturesite_id, comment= c)    

    c.text = request.form.get("newtext")
    db.session().commit()
  
    return redirect(url_for("show_comments", report_id = report_id, naturesite_id=naturesite_id)) 


@app.route("/comment/<report_id>/<naturesite_id>/<comment_id>/delete/", methods=["POST"])
@login_required
def delete_comment(report_id, naturesite_id, comment_id):

    r = Report.query.get(report_id)

    if not r:
        return render_template("error.html",  message = "ERROR! Report not found")  
    
    n = NatureSite.query.get(naturesite_id)
    
    if not n:
        return render_template("error.html",  message = "ERROR! Nature site not found")
    
    c = Comment.query.get(comment_id)

    if not c:
        return render_template("error.html",  message = "ERROR! Comment not found")

    if c.account_id != current_user.id:
        return login_manager.unauthorized()

    db.session.delete(c)
    db.session().commit()
  
    return redirect(url_for("show_comments", report_id = report_id, naturesite_id=naturesite_id)) 

@app.route("/comment/<report_id>/<naturesite_id>/<comment_id>/", methods=["GET"])
@login_required
def comment_edit(report_id, naturesite_id, comment_id):

    r = Report.query.get(report_id)
    
    if not r:
        return render_template("error.html",  message = "ERROR! Report not found")  
    
    n = NatureSite.query.get(naturesite_id)
    
    if not n:
        return render_template("error.html",  message = "ERROR! Nature site not found")

    c = Comment.query.get(comment_id)

    if not c:
        return render_template("error.html",  message = "ERROR! Comment not found")

    if c.account_id != current_user.id:
        return login_manager.unauthorized()
    
    return render_template("comment/edit.html", form=CommentEditForm(), report_id = report_id, naturesite_id = naturesite_id, comment = Comment.query.get(comment_id))     

