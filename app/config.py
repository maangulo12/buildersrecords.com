# -*- coding: utf-8 -*-

"""
    config.py
    ~~~~~~~~~~~~

    This module implements all of the static variables for this application.
"""

APP_SECRET_KEY      = 'secret_key'

SERVER_HOST         = '0.0.0.0'
SERVER_PORT         =  5555
DEBUG_FLAG          =  True

DB_ENGINE           = 'postgresql'
DB_USERNAME         = 'postgres'
DB_PASSWORD         = 'password'
DB_SERVER           = 'localhost'
DB_PORT             = '5432'
DB_NAME             = 'app_db'

MAIL_SERVER         = 'smtp.gmail.com'
MAIL_PORT           =  465
MAIL_USE_SSL        =  True
MAIL_USERNAME       = 'buildersrecords.app@gmail.com'
MAIL_PASSWORD       = 'buildersrecords123'
MAIL_DEFAULT_SENDER = ('BuildersRecords', 'buildersrecords.app@gmail.com')
