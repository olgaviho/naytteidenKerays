from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NewCommentForm(FlaskForm):
    text = StringField("text", [validators.Length(min=3)])

    class Meta:
        csrf = False

class CommentEditForm(FlaskForm):

    text = StringField("Edit text")

    class Meta:
        csrf = False           
