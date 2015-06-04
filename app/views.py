# -*- coding: utf-8 -*-

"""
    views.py
    ~~~~~~~~~~~~

    This module implements all of the views / routes of this application.

"""


from flask import render_template

from app import app


@app.route('/')
def home():
    """
    Route for url: server/
    """
    return render_template('home.html')
