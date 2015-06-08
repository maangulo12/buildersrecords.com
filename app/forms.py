# -*- coding: utf-8 -*-

"""
    forms.py
    ~~~~~~~~~~~~

    This module implements the classes for creating and validating forms.
"""

from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired

from app.db import get_cursor
from app.utility import check_password
from app.data.users import *


class SignupForm(Form):
    first_name       = StringField  ('First Name',       [DataRequired(), validators.Length(max=30)])
    last_name        = StringField  ('Last Name',        [DataRequired(), validators.Length(max=30)])
    email            = StringField  ('Email',            [DataRequired(), validators.Length(max=50)])
    username         = StringField  ('Username',         [DataRequired(), validators.Length(max=25)])
    password         = PasswordField('Password',         [DataRequired(), validators.Length(min=5, max=40)])
    confirm_password = PasswordField('Confirm Password', [DataRequired(), validators.Length(min=5, max=40)])

    def validate(self):
        """
        Checks if the form is valid and validates the email, username, and password.

        :return: False if email or username or password are not valid.
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

        if self.password.data != self.confirm_password.data:
            self.password.errors.append('Password does not match.')
            self.confirm_password.errors.append('')
            return False

        return True


class LoginForm(Form):
    username = StringField  ('Username or Email', [DataRequired()])
    password = PasswordField('Password',          [DataRequired()])

    def authenticate(self):
        """
        Checks if the form is valid and authenticates the user by checking email or username and password.

        :return: False if user is not valid.
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
