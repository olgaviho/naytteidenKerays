from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NewCommentForm(FlaskForm):
    text = StringField("text", [validators.Length(min=1, max= 50)])

    class Meta:
        csrf = False

class CommentEditForm(FlaskForm):

    newtext = StringField("Edit text", [validators.Length(min=1, max = 50)] )

    class Meta:
        csrf = False           
