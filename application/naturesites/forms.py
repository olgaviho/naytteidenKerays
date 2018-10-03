from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NatureSiteForm(FlaskForm):
    name = StringField("Nature site name", [validators.Length(min=2)])
    description = StringField("Description")

    class Meta:
        csrf = False
        
class NatureSiteEditForm(FlaskForm):

    description = StringField("Edit description")

    class Meta:
        csrf = False        