# -*- coding: utf-8 -*-

"""
    BuildersRecords
    ---------------

    Run this to deploy this application.

"""


import os

from app import app


if __name__ == '__main__':
    app.run(
        host=os.environ.get('SERVER_HOST', '0.0.0.0'),
        port=int(os.environ.get('SERVER_PORT', '5555')),
        debug=True
    )
