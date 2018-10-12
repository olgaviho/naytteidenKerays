from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class CreateAccountForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max = 12)])
    username = StringField("Username", [validators.Length(min=2, max = 12)])  
    password = PasswordField("Password", [validators.Length(min=6, max = 20)]) 
    password2 = PasswordField("Write password again", [validators.Length(min=6, max = 20)]) 

    class Meta:
        csrf = False     