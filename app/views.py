# -*- coding: utf-8 -*-

"""
    views.py
    ~~~~~~~~~~~~

    This module implements all of the views / routes of this application.
"""

from flask import *

from app.db import get_cursor
from app.utility import hash_password
from app.forms import SignupForm, LoginForm, PasswordResetForm
from app.mail import send_registration_email, send_password_reset_email
from app.data.users import *
from app.data.projects import *
from app import app, csrf


@app.route('/')
def home():
    """
    Route for url: server/
    """
    if 'username' in session:
        cur = get_cursor()
        user_id      = get_user_id(cur, session['username'])
        project_list = get_project_list(cur, user_id)
        return render_template('user_home.html', username     = session['username'],
                                                 project_list = project_list)

    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(e):
    """
    Route for url: 404 page not found error
    """
    return render_template('404_error.html')


@csrf.error_handler
def csrf_error(reason):
    """
    Route for url: csrf error
    """
    return render_template('csrf_error.html', reason = reason)


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    """
    Route for url: server/signup/
    """
    form = SignupForm()
    if request.method == 'GET':
        return render_template('signup.html', form = form)

    if request.method == 'POST':
        if form.validate():
            cur = get_cursor()
            pw_hash = hash_password(form.password.data)
            add_user(cur, form, pw_hash)
            send_registration_email(form)
            session['username'] = form.username.data
            flash('Welcome to BuildersRecords! Thank you for creating an account.')
            return redirect(url_for('home'))

        flash('There were problems creating your account.')
        return render_template('signup.html', form = form)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    """
    Route for url: server/login/
    """
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form = form)

    if request.method == 'POST':
        if form.authenticate():
            session['username'] = form.username.data
            flash('You have successfully logged in! Get started by choosing a project.')
            return redirect(url_for('home'))

        flash('Incorrect username / password combination. Please try again.')
        return render_template('login.html', form = form)


@app.route('/logout/')
def logoff():
    """
    Route for url: server/logout/
    """
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for('login'))

    return abort(404)


@app.route('/password_reset/', methods=['GET', 'POST'])
def password_reset():
    """
    Route for url: server/password_reset/
    """
    form = PasswordResetForm()
    if request.method == 'GET':
        return render_template('password_reset.html', form = form)

    if request.method == 'POST':
        if form.validate():
            send_password_reset_email(form.email.data)
            return render_template('password_reset_confirmation.html')

        flash('Could not find that email. Please try again.')
        return render_template('password_reset.html', form = form)
