# -*- coding: utf-8 -*-

"""
    config.py
    ~~~~~~~~~~~~

    This module implements all of the config variables for this application.
"""

import os


# App Key
SECRET_KEY          =  os.environ.get('SECRET_KEY', 'secret_key')

# WSGI Server
SERVER_HOST         =  os.environ.get('SERVER_HOST', '0.0.0.0')
SERVER_PORT         =  int(os.environ.get('SERVER_PORT', 5555))
DEBUG_FLAG          =  True

# Local DB Settings
DB_ENGINE           = 'postgresql'
DB_USERNAME         = 'postgres'
DB_PASSWORD         = 'password'
DB_SERVER           = 'localhost'
DB_PORT             = '5432'
DB_NAME             = 'app_db'

# Production DB Settings
DATABASE_URL        =  os.environ.get('DATABASE_URL', DB_ENGINE + '://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_SERVER + ':' + DB_PORT + '/' + DB_NAME)

# Email Service
MAIL_SERVER         = 'smtp.gmail.com'
MAIL_PORT           =  465
MAIL_USE_SSL        =  True
MAIL_USERNAME       =  os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD       =  os.environ.get('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER =  ('BuildersRecords', MAIL_USERNAME)

# Uploads
UPLOAD_FOLDER       =  os.environ.get('UPLOAD_FOLDER', '/uploads/')
ALLOWED_EXTENSIONS  =  set(['xlsx', 'xls'])
