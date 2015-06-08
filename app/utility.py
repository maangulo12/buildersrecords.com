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

    :param password: string
    :return: password hashed
    """
    return hashpw(password.encode('utf-8'), gensalt(12)).decode('utf-8')
