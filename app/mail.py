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
    This function sends a registration email.
    """
    msg = Message("Thank you from BuildersRecords", recipients=[form.email.data])
    msg.html = render_template('email/registration.html', username = form.username.data,
                                                          password = form.password.data)
    mail.send(msg)
