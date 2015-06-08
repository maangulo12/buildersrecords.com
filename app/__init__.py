# -*- coding: utf-8 -*-

"""
    BuildersRecords
    ~~~~~~~~~~~~~~~

    A web application for budgeting construction projects.

    :copyright: (c) 2015 by Miguel Angulo.
"""

from flask import Flask
from flask_mail import Mail
from flask_wtf.csrf import CsrfProtect

from app.config import *


app = Flask(__name__)
app.secret_key = APP_SECRET_KEY

# MAIL SERVICE
app.config.update(
    MAIL_SERVER         = MAIL_SERVER,
    MAIL_PORT           = MAIL_PORT,
    MAIL_USE_SSL        = MAIL_USE_SSL,
    MAIL_USERNAME       = MAIL_USERNAME,
    MAIL_PASSWORD       = MAIL_PASSWORD,
    MAIL_DEFAULT_SENDER = MAIL_DEFAULT_SENDER
)
mail = Mail(app)

# CSRF PROTECTION
csrf = CsrfProtect()
csrf.init_app(app)


from app import config
from app import db
from app import forms
from app import mail
from app import utility
from app import views
