from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NewReportForm(FlaskForm):
    name = StringField("Report name", [validators.Length(min=2)])
    description = StringField("Description")

    class Meta:
        csrf = False