from application import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.report.models import Report
from application.report.forms import NewReportForm


