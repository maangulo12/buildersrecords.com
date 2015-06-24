#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    db.py
    ~~~~~~~~~~~~

    This module implements the methods for accessing the database.
"""

from psycopg2 import connect, Error
from urllib.parse import uses_netloc, urlparse
from flask import g

from app import app
from app.config import DATABASE_URL


def connect_db(autocommit = True):
    """
    Creates a connection to the PostgreSQL database server.

    :return: Database connection
    """
    uses_netloc.append('postgres')
    url = urlparse(DATABASE_URL)

    try:
        conn = connect(
            database = url.path[1:],
            user     = url.username,
            password = url.password,
            host     = url.hostname,
            port     = url.port
        )
        conn.autocommit = autocommit
        return conn

    except Error as e:
        print(e)


def get_cursor():
    """
    Gets database cursor. Calls connect_db() to create a connection.

    :return: Database cursor
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_db()
    return db.cursor()


@app.teardown_appcontext
def teardown_db(e):
    """
    Method is called at the end of each request regardless of whether
    there was an exception or not. It teardowns database connection if there was one.

    :param e: exception
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
