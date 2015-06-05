# -*- coding: utf-8 -*-

"""
    BuildersRecords
    ~~~~~~~~~~~~

    A web application for budgeting construction projects.

"""


from flask import *
from flask_wtf.csrf import CsrfProtect


app = Flask(__name__)
app.secret_key = 'secret_key'

csrf = CsrfProtect()
csrf.init_app(app)


@csrf.error_handler
def csrf_error(reason):
    """
    Route for url: csrf error
    """
    return render_template('csrf_error.html', reason=reason)


from app import db
from app import forms
from app import mail
from app import views
