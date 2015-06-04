# -*- coding: utf-8 -*-

"""
    BuildersRecords
    ~~~~~~~~~~~~

    A web application for budgeting construction projects.

"""


from flask import Flask


app = Flask(__name__)

from app import views
