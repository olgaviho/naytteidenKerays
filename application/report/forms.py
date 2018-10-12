from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NewReportForm(FlaskForm):
    title = StringField("Title", [validators.Length(min=3, max = 12)])
    description = StringField("Description", [validators.Length(min=3,max=20)])

    class Meta:
        csrf = False


class ReportEditForm(FlaskForm):

    description = StringField("Edit description", [validators.Length(min=3,max=20)])

    class Meta:
        csrf = False         