# -*- coding: utf-8 -*-

"""
    app_tests.py
    ~~~~~~~~~~~~

    This module implements the methods for testing this application.
"""

import os
import unittest
import tempfile

import app from app


class FlaskrTestCase(unittest.TestCase):


    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()


    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])


if __name__ == '__main__':
    unittest.main()
