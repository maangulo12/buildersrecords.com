# -*- coding: utf-8 -*-

"""
    views.py
    ~~~~~~~~~~~~

    This module implements all of the views / routes of this application.

"""


from flask import *

from app.db import get_cursor, hash_password
from app.forms import SignupForm
from app.mail import send_registration_email
from app.data.users import *
from app import app


@app.route('/')
def home():
    """
    Route for url: server/
    """
    return render_template('home.html')


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
            add_user(cur, form, pw_hash.decode('utf-8'))
            send_registration_email(form)
            session['username'] = form.username.data
            return redirect(url_for('home'))

        flash('There were problems creating your account.')
        return redirect(url_for('signup')) 
