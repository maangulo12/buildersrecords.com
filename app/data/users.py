# -*- coding: utf-8 -*-

"""
Functions for CRUD content from the users table.
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
