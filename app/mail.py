# -*- coding: utf-8 -*-

"""
    mail.py
    ~~~~~~~~~~~~

    This module implements the methods for email service.
"""

from flask import render_template
from flask_mail import Message

from app import mail


def send_registration_email(form):
    """
    This method sends a registration email.
    """
    msg = Message("Thank you from BuildersRecords", recipients=[form.email.data])
    msg.html = render_template('email/registration.html', username = form.username.data,
                                                          first_name = form.first_name.data,
                                                          last_name = form.last_name.data)
    mail.send(msg)


def send_password_reset_email(email):
    """
    This method sends an email to reset password.
    """
    msg = Message("Reset your password", recipients=[email])
    msg.html = render_template('email/password_reset.html')
    mail.send(msg)
