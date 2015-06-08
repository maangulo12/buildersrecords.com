# -*- coding: utf-8 -*-

"""
    utility.py
    ~~~~~~~~~~~~

    This module implements the methods for hashing and checking passwords.
"""

from bcrypt import hashpw, gensalt


def hash_password(password):
    """
    Hashes the password using bcrypt.

    :param password: a string
    :return: password hashed
    """
    return hashpw(password.encode('utf-8'), gensalt(12)).decode('utf-8')


def check_password(password, pw_hash):
    """
    Checks if the password matches the hashed password.

    :param password: a string
    :param pw_hash: password hash
    :return: True if they match
    """
    return hashpw(password.encode('utf-8'), pw_hash.encode('utf-8')) == pw_hash.encode('utf-8')
