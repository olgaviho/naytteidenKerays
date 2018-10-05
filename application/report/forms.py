from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NewReportForm(FlaskForm):
    title = StringField("Title", [validators.Length(min=2)])
    description = StringField("Description")

    class Meta:
        csrf = False


class ReportEditForm(FlaskForm):

    description = StringField("Edit description")

    class Meta:
        csrf = False         