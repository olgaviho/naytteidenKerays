from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NatureSiteForm(FlaskForm):
    name = StringField("Nature site name", [validators.Length(min=3, max=12)])
    description = StringField("Description",[validators.Length(min=3, max = 20)])

    class Meta:
        csrf = False
        
class NatureSiteEditForm(FlaskForm):

    description = StringField("Edit description",[validators.Length(min=3, max=20)])

    class Meta:
        csrf = False        