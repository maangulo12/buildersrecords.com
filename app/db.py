#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    db.py
    ~~~~~~~~~~~~

    This module implements the functions for accessing the PostgreSQL database. It also includes the functions for
    hashing and checking passwords.

"""

import os
from bcrypt import hashpw, gensalt
from psycopg2 import connect, Error
from urllib.parse import uses_netloc, urlparse
from flask import g

from app import app


def connect_db():
    """
    Creates a connection to the PostgreSQL database server.

    :return: Database connection
    """
    uses_netloc.append('postgres')
    url = urlparse(os.environ["DATABASE_URL"])

    try:
        conn = connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
        conn.autocommit = True
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
    Function is called at the end of each request regardless of whether
    there was an exception or not. It teardowns database connection if there was one.

    :param e: exception
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def hash_password(password):
    """
    Hashes the password using bcrypt.

    :param password: password characters
    :return: password hashed
    """
    return hashpw(password.encode('utf-8'), gensalt(12))
