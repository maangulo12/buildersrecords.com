# -*- coding: utf-8 -*-

"""
    mail.py
    ~~~~~~~~~~~~

    This module adds mail service to the application.

"""


from flask_mail import Mail, Message

from app import app


app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='shumadda@gmail.com',
    MAIL_PASSWORD='total90411568',
    MAIL_DEFAULT_SENDER=("BuildersRecords", "shumadda@gmail.com")
)
mail = Mail(app)


def send_registration_email(form):
    """
    This function sends out a registration email.
    """
    msg = Message("Welcome to BuildersRecords", recipients=[form.email.data])
    msg.html = "Welcome to BuildersRecords," + "<br>" + \
               "<br>" + \
               "Thank you for creating an account with us." + "<br>" + \
               "<br>" + \
               "Your username is: " + "<b>" + form.username.data + "</b>" + "<br>" + \
               "Your password is: " + "<b>" + form.password.data + "</b>" + "<br>" + \
               "<br>" + \
               "-From the BuildersRecords team"
    mail.send(msg)
