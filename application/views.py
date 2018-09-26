from flask import render_template
from application import app
from application.auth.models import User

@app.route("/")
def index():
    return render_template("index.html")
# users_and_naturesites=User.how_many_naturesites_users_have())
    