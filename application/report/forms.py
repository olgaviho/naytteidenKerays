from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NewReportForm(FlaskForm):
    title = StringField("Title", [validators.Length(min=3, max = 20)])
    description = StringField("Description", [validators.Length(min=1,max=30)])

    class Meta:
        csrf = False


class ReportEditForm(FlaskForm):

    description = StringField("Edit description", [validators.Length(min=1,max=30)])

    class Meta:
        csrf = False         
