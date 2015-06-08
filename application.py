# -*- coding: utf-8 -*-

"""
    BuildersRecords
    ---------------

    Run this to deploy this application.

    :copyright: (c) 2015 by Miguel Angulo.
"""

import os

from app import app
from app.config import *


if __name__ == '__main__':
    app.run(
        host  = os.environ.get('SERVER_HOST', SERVER_HOST),
        port  = int(os.environ.get('SERVER_PORT', SERVER_PORT)),
        debug = DEBUG_FLAG
    )
