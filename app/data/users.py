# -*- coding: utf-8 -*-

"""
    users.py
    ~~~~~~~~~~~~

    This module implements the methods for CRUD content for the users table.
"""

# Check if username exists
def username_exists(cur, username):
    cur.execute('''
        SELECT COUNT(username)
        FROM users
        WHERE username = %s
    ''', (username,))

    (count,) = cur.fetchone()
    if count == 1:
        return True


# Check if email exists
def email_exists(cur, email):
    cur.execute('''
        SELECT COUNT(email)
        FROM users
        WHERE email = %s
    ''', (email,))

    (count,) = cur.fetchone()
    if count == 1:
        return True


# Insert a new user into users table
def add_user(cur, form, pw_hash):
    cur.execute('''
        INSERT INTO users (username, pw_hash, first_name, last_name, email)
        VALUES (%s, %s, %s, %s, %s)
        ''', (form.username.data,
              pw_hash,
              form.first_name.data,
              form.last_name.data,
              form.email.data))


# Get username from given email
def get_username(cur, email):
    cur.execute('''
        SELECT username
        FROM users
        WHERE email = %s
    ''', (email,))

    (username,) = cur.fetchone()
    if username is not None:
        return username


# Get password hash for a given username
def get_pw_hash(cur, username):
    cur.execute('''
        SELECT pw_hash
        FROM users
        WHERE username = %s
    ''', (username,))

    (pw_hash,) = cur.fetchone()
    if pw_hash is not None:
        return pw_hash


# Get user_id from username
def get_user_id(cur, username):
    cur.execute('''
        SELECT user_id
        FROM users
        WHERE username = %s
    ''', (username,))

    (user_id,) = cur.fetchone()
    if user_id is not None:
        return user_id
