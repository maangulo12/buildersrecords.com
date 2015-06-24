# -*- coding: utf-8 -*-

"""
    views.py
    ~~~~~~~~~~~~

    This module implements all of the views / routes of this application.
"""

from flask import *

from app.db import get_cursor
from app.utility import hash_password, upload_file, check_file, parse_file, get_color, get_hightlight_color
from app.forms import SignupForm, LoginForm, PasswordResetForm, AccountForm, PasswordForm, NewForm, UploadForm
from app.mail import send_registration_email, send_password_reset_email
from app.data.users import *
from app.data.projects import *
from app.data.categories import *
from app import app, csrf


@app.route('/')
def home():
    """
    Route for url: server/
    """
    if 'username' in session:
        cur                = get_cursor()
        session['user_id'] = get_user_id(cur, session['username'])
        project_list       = get_project_list(cur, session['user_id'])
        return render_template('user_home.html', username     = session['username'],
                                                 project_list = project_list)
    return render_template('home.html')


@app.route('/signup/', methods = ['GET', 'POST'])
def signup():
    """
    Route for url: server/signup/
    """
    form = SignupForm()
    if request.method == 'GET':
        return render_template('signup.html', form = form)

    if request.method == 'POST':
        if form.validate():
            cur     = get_cursor()
            pw_hash = hash_password(form.password.data)
            add_user(cur, form, pw_hash)
            send_registration_email(form)
            session['username'] = form.username.data
            flash('Welcome to BuildersRecords! Thank you for creating an account with us.')
            return redirect(url_for('home'))
        flash('There were problems creating your account.')
        return render_template('signup.html', form = form)


@app.route('/login/', methods = ['GET', 'POST'])
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
            return redirect(url_for('home'))
        flash('Incorrect username / password combination. Please try again.')
        return render_template('login.html', form = form)


@app.route('/logout/')
def logout():
    """
    Route for url: server/logout/
    """
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for('login'))
    return abort(404)


@app.route('/password_reset/', methods = ['GET', 'POST'])
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


@app.route('/settings/account/', methods = ['GET', 'POST'])
def account():
    """
    Route for url: server/settings/account/
    """
    if 'username' in session:
        form = AccountForm()
        if request.method == 'GET':
            cur                  = get_cursor()
            user_data            = get_user_data(cur, session['username'])
            form.first_name.data = user_data['first_name']
            form.last_name.data  = user_data['last_name']
            form.email.data      = user_data['email']
            return render_template('account.html', form     = form,
                                                   username = session['username'])

        if request.method == 'POST':
            if form.validate():
                cur = get_cursor()
                update_user_data(cur, form, session['username'])
                flash('Your account information has been successfully updated!')
                return redirect(url_for('account'))
            return render_template('account.html', form     = form,
                                                   username = session['username'])
    return abort(404)


@app.route('/settings/password/', methods = ['GET', 'POST'])
def password():
    """
    Route for url: server/settings/password/
    """
    if 'username' in session:
        form = PasswordForm()
        if request.method == 'GET':
            return render_template('password.html', form     = form,
                                                    username = session['username'])

        if request.method == 'POST':
            if form.validate():
                cur     = get_cursor()
                pw_hash = hash_password(form.new_password.data)
                update_password(cur, pw_hash, session['username'])
                flash('Your password has been successfully updated!')
                return redirect(url_for('password'))
            return render_template('password.html', form     = form,
                                                    username = session['username'])
    return abort(404)


@app.route('/new/', methods = ['GET', 'POST'])
def new():
    """
    Route for url: server/new/
    """
    if 'username' in session:
        form = NewForm()
        if request.method == 'GET':
            session.pop('project_name', None)
            session.pop('project_type', None)
            return render_template('new.html', form     = form,
                                               username = session['username'])

        if request.method == 'POST':
            if form.validate():
                session['project_name'] = form.project_name.data
                if form.project_type.data == 'create':
                    session['project_type'] = 'Create My Own'
                    session['data_parsed'] = ''
                    return redirect(url_for('edit'))
                if form.project_type.data == 'ubuildit':
                    session['project_type'] = 'UBuildIt'
                    return redirect(url_for('upload'))
            flash('There were problems creating your project.')
            return render_template('new.html', form     = form,
                                               username = session['username'])
    return abort(404)


@app.route('/new/upload/', methods = ['GET', 'POST'])
def upload():
    """
    Route for url: server/new/upload/
    """
    if 'username' in session:
        form = UploadForm()
        if request.method == 'GET':
            session['data_parsed'] = ''
            if 'project_name' in session and 'project_type' in session:
                return render_template('ubuildit.html', form     = form,
                                                        username = session['username'])
        if request.method == 'POST':
            if form.validate():
                file = request.files['file']
                if upload_file(file):
                    if check_file(file):
                        session['data_parsed'] = parse_file(file)
                        flash('Your file has been successfully uploaded!')
                        return redirect(url_for('preview'))
                    else:
                        flash('This file is invalid.')
                else:
                    flash('Could not upload your excel file.')
            else:
                flash('There were problems with your file.')
            return render_template('ubuildit.html', form     = form,
                                                    username = session['username'])
    return abort(404)


@app.route('/new/preview/')
def preview():
    """
    Route for url: server/new/preview/
    """
    if 'username' in session:
        if 'project_name' in session and 'project_type' in session:
            return render_template('preview.html', username     = session['username'],
                                                   project_name = session['project_name'],
                                                   categories   = session['data_parsed'])
    return abort(404)


@app.route('/new/edit/', methods = ['GET', 'POST'])
def edit():
    """
    Route for url: server/new/edit/
    """
    if 'username' in session:
        if request.method == 'GET':
            if 'project_name' in session and 'project_type' in session:
                return render_template('edit.html', username     = session['username'],
                                                    project_name = session['project_name'],
                                                    categories   = session['data_parsed'])
    return abort(404)


@app.route('/new/create/')
def create():
    """
    Route for url: server/new/create/
    """
    if 'username' in session:
        if 'project_name' in session and 'project_type' in session and session['data_parsed'] != '':
            cur = get_cursor()
            create_project(cur, session['project_name'], session['project_type'], session['data_parsed'], session['user_id'])
            project_id = get_project_id(cur, session['project_name'], session['user_id'])
            session.pop('project_name', None)
            session.pop('project_type', None)
            session['data_parsed'] = ''
            return redirect(url_for('dashboard', username   = session['username'],
                                                 project_id = project_id))
    return abort(404)


@app.route('/<username>/<int:project_id>/dashboard/')
def dashboard(username, project_id):
    """
    Route for url: server/<username>/<project_id>/dashboard/
    """
    if 'username' in session:
        cur = get_cursor()
        if username == session['username'] and project_id_exists(cur, project_id):
            session['project_id'] = project_id
            project_detail = get_project_detail(cur, project_id)
            category_list  = get_category_list(cur, project_id)
            return render_template('dashboard.html', username       = session['username'],
                                                     project_detail = project_detail,
                                                     category_list  = category_list)
    return abort(404)


#------------------------------ AJAX VIEWS -------------------------------
@app.route('/delete_project_ajax/')
def delete_project_ajax():
    """
    AJAX
    Route for url: server/delete_project/
    """
    if 'username' in session:
        project_id = request.args.get('project_id', 0, type = int)
        cur        = get_cursor()
        remove_project(cur, session['user_id'], project_id)
        return jsonify(msg = 'Project removed')
    return abort(404)


@app.route('/dashboard_ajax/')
def dashboard_ajax():
    """
    AJAX
    Route for url: server/dashboard_ajax/
    """
    if 'username' in session:
        cur          = get_cursor()
        categories   = get_category_list(cur, session['project_id'])
        data         = []
        counter      = 0
        total_budget = 0
        total_spent  = 0
        for category in categories:
            category_budget = 0
            category_spent  = 0
            for item in category['item_list']:
                category_budget += item['budget']
                category_spent  += item['actual']

            data.append(
                {
                    'value':     int(category_spent),
                    'color':     get_color(counter),
                    'highlight': get_hightlight_color(counter),
                    'label':     category['category_name']
                })

            total_budget += category_budget
            total_spent  += category_spent
            counter += 1
        # Append amount left
        data.append(
            {
                'value':         int(total_budget - total_spent),
                'color':         '#FDB45C',
                'highlight':     '#FFC870',
                'label':         'Amount Left',
            })
        return jsonify(data = data)
    return abort(404)


# --------------------------- ERROR VIEWS --------------------------------
@app.errorhandler(404)
def page_not_found(e):
    """
    Route for url: 404 page not found error
    """
    return render_template('error/404_error.html')


@app.errorhandler(405)
def method_not_allowed(e):
    """
    Route for url: 405 method not allowed error
    """
    return render_template('error/405_error.html')


@csrf.error_handler
def csrf_error(reason):
    """
    Route for url: csrf error
    """
    return render_template('error/csrf_error.html', reason = reason)
