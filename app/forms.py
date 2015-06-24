# -*- coding: utf-8 -*-

"""
    forms.py
    ~~~~~~~~~~~~

    This module implements the classes for creating and validating forms.
"""

from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp
from flask import session, request

from app.db import get_cursor
from app.utility import check_password, allowed_file
from app.data.users import *
from app.data.projects import *


class SignupForm(Form):
    first_name       = StringField  ('First Name',       [DataRequired(), Length(max = 30)])
    last_name        = StringField  ('Last Name',        [DataRequired(), Length(max = 30)])
    email            = StringField  ('Email',            [DataRequired(), Length(max = 50),          Email()])
    username         = StringField  ('Username',         [DataRequired(), Length(max = 25),          Regexp(r'^[\w.@+-]+$',      message = 'No spaces allowed.' )])
    password         = PasswordField('Password',         [DataRequired(), Length(min = 5, max = 40), EqualTo('confirm_password', message = 'Passwords must match.')])
    confirm_password = PasswordField('Confirm Password', [DataRequired(), Length(min = 5, max = 40), EqualTo('password',         message = '')])

    def validate(self):
        """
        Checks if the form is valid and validates the email, username, and password.

        :return: False if the email or username or password are not valid.
        """
        rv = Form.validate(self)
        if not rv:
            return False

        cur = get_cursor()
        if email_exists(cur, self.email.data):
            self.email.errors.append('This email already exists!')
            return False

        if username_exists(cur, self.username.data):
            self.username.errors.append('This username already exists!')
            return False

        return True


class LoginForm(Form):
    username = StringField  ('Username or Email', [DataRequired()])
    password = PasswordField('Password',          [DataRequired()])

    def authenticate(self):
        """
        Checks if the form is valid and authenticates the user by checking email or username and password.

        :return: False if the user is not valid.
        """
        rv = Form.validate(self)
        if not rv:
            return False

        user = self.username.data

        cur = get_cursor()
        if email_exists(cur, user):
            user = get_username(cur, user)

        if username_exists(cur, user):
            pw_hash = get_pw_hash(cur, user)

            if check_password(self.password.data, pw_hash):
                self.username.data = user
                return True

        return False


class PasswordResetForm(Form):
    email = StringField('Email Address', [DataRequired(), Email()])

    def validate(self):
        """
        Checks if the form is valid and validates the email address.

        :return: False if the email address is not valid.
        """
        rv = Form.validate(self)
        if not rv:
            return False

        cur = get_cursor()
        if not email_exists(cur, self.email.data):
            self.email.errors.append('Please check your email address.')
            return False

        return True


class AccountForm(Form):
    first_name = StringField('First Name', [DataRequired(), Length(max = 30)])
    last_name  = StringField('Last Name',  [DataRequired(), Length(max = 30)])
    email      = StringField('Email',      [DataRequired(), Length(max = 50), Email()])

    def validate(self):
        """
        Checks if the form is valid and validates the email.

        :return: False if the email is not valid.
        """
        rv = Form.validate(self)
        if not rv:
            return False

        cur = get_cursor()
        if email_exists(cur, self.email.data):
            self.email.errors.append('This email already exists!')
            return False

        return True


class PasswordForm(Form):
    old_password     = PasswordField('Old Password',     [DataRequired(), Length(min = 5, max = 25)])
    new_password     = PasswordField('New Password',     [DataRequired(), Length(min = 5, max = 25), EqualTo('confirm_password', message = 'Passwords must match.')])
    confirm_password = PasswordField('Confirm Password', [DataRequired(), Length(min = 5, max = 25), EqualTo('new_password',     message = '')])

    def validate(self):
        """
        Checks if the form is valid and validates the old and new passwords.

        :return: False if the old or new passwords are not valid.
        """
        rv = Form.validate(self)
        if not rv:
            return False

        cur     = get_cursor()
        pw_hash = get_pw_hash(cur, session['username'])
        if not check_password(self.old_password.data, pw_hash):
            self.old_password.errors.append('Did not find a match.')
            return False

        return True


class NewForm(Form):
    project_name = StringField('Project Name',    [DataRequired(),  Length(max = 50)])
    project_type = SelectField('Type of Project', [DataRequired()], choices = [('create', 'Create my own'), ('ubuildit', 'UBuildIt'),])

    def validate(self):
        """
        Checks if the form is valid and validates the project name and project type.

        :return: False if the project name or project type are not valid.
        """
        rv = Form.validate(self)
        if not rv:
            return False

        cur     = get_cursor()
        user_id = get_user_id(cur, session['username'])
        if project_name_exists(cur, self.project_name.data, user_id):
            self.project_name.errors.append('A project already exists with that name.')
            return False

        return True


class UploadForm(Form):
    file = FileField('Excel File', [DataRequired()])

    def validate(self):
        """
        Checks if the form is valid and validates the file extension.

        :return: False if the file extension is not valid.
        """
        rv = Form.validate(self)
        if not rv:
            return False

        file = request.files['file']
        if not file:
            self.file.errors.append('Could not find your file.')
            return False

        if not allowed_file(file.filename):
            self.file.errors.append('Only excel files can be uploaded (only .xls or .xlsx )')
            return False

        return True
