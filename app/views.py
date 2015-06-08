# -*- coding: utf-8 -*-

"""
    views.py
    ~~~~~~~~~~~~

    This module implements all of the views / routes of this application.
"""

from flask import *

from app.db import get_cursor
from app.utility import hash_password
from app.forms import SignupForm
from app.mail import send_registration_email
from app.data.users import *
from app import app, csrf


@app.route('/')
def home():
    """
    Route for url: server/
    """
    return render_template('home.html')


@csrf.error_handler
def csrf_error(reason):
    """
    Route for url: csrf error
    """
    return render_template('csrf_error.html', reason=reason)


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    """
    Route for url: server/signup/
    """
    form = SignupForm()
    if request.method == 'GET':
        return render_template('signup.html', form=form)

    if request.method == 'POST':
        if form.validate():
            cur = get_cursor()
            pw_hash = hash_password(form.password.data)
            add_user(cur, form, pw_hash)
            send_registration_email(form)
            session['username'] = form.username.data
            return redirect(url_for('home'))

        flash('There were problems creating your account.')
        return render_template('signup.html', form=form)
