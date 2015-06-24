# -*- coding: utf-8 -*-

"""
    utility.py
    ~~~~~~~~~~~~

    This module implements the utility methods for this application.
"""

import os
import sys
from bcrypt import hashpw, gensalt
from xlrd import open_workbook
from werkzeug import secure_filename

from app.config import ALLOWED_EXTENSIONS, UPLOAD_FOLDER


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


def allowed_file(filename):
    """
    Checks filename extension to see if allowed.

    :param filename: name of the file
    :return: True if filename extension is allowed
    """
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def upload_file(file):
    """
    Saves a file to UPLOAD_FOLDER.

    :param file: a file object
    :return: True if the file is saved
    """
    try:
        filename = secure_filename(file.filename)
        location = os.path.join(UPLOAD_FOLDER, filename)
        file.save(location)
        return True

    except:
        print("Unexpected error:", sys.exc_info()[0])
        return False


def check_file(file):
    """
    Checks the excel file.

    :param file: a file object
    :return: True if the file is the correct file
    """
    try:
        filename = secure_filename(file.filename)
        wb = open_workbook(filename = ''.join([UPLOAD_FOLDER, filename]))
        ws = wb.sheet_by_name('UBI Cost Review')
        return True

    except:
        print("Unexpected error:", sys.exc_info()[0])
        return False


def parse_file(file):
    """
    Parses the UBuildIt excel file.

    :param file: a file object
    :return: True if file is successfully parsed
    """
    filename = secure_filename(file.filename)
    wb = open_workbook(filename = ''.join([UPLOAD_FOLDER, filename]))
    ws = wb.sheet_by_name('UBI Cost Review')

    categories = []
    categories.append({'category_name': ws.cell_value(5 , 2), 'item_list': get_item_list(ws, 6 , 15)})  # Pre-Construction Costs
    categories.append({'category_name': ws.cell_value(16, 2), 'item_list': get_item_list(ws, 17, 33)})  # Site Development Costs
    categories.append({'category_name': ws.cell_value(34, 2), 'item_list': get_item_list(ws, 35, 43)})  # Site Preparation
    categories.append({'category_name': ws.cell_value(44, 2), 'item_list': get_item_list(ws, 45, 47)})  # Foundation
    categories.append({'category_name': ws.cell_value(48, 2), 'item_list': get_item_list(ws, 49, 52)})  # Slab Work
    categories.append({'category_name': ws.cell_value(53, 2), 'item_list': get_item_list(ws, 54, 60)})  # Main Structure
    categories.append({'category_name': ws.cell_value(61, 2), 'item_list': get_item_list(ws, 62, 93)})  # General Trades
    categories.append({'category_name': ws.cell_value(94, 2), 'item_list': get_item_list(ws, 95, 130)}) # Interior Finishing
    return categories


def get_item_list(ws, start, end):
    """
    Get item list for parsing excel file.

    :param start: start position to read row of file
    :param end: end position to read row of file
    :return: Returns the item_list parsed
    """
    temp_list = []

    for i in range(start, end):
        cells = ws.row_slice(rowx       = i,
                             start_colx = 2,
                             end_colx   = 10)

        temp_list.append({
            'cost_category':     cells[0].value,
            'notes':             cells[1].value,
            'budget':            convert_to_float(cells[2].value),
            'actual':            convert_to_float(cells[3].value),
            'change_orders':     cells[4].value,
            'over_under_budget': cells[5].value,
            'total_cost':        cells[6].value,
            'explanations':      cells[7].value
        })
    return temp_list


def convert_to_float(s):
    """
    Method for converting a string into int or float.

    :param s: string
    :return: Returns an int or float
    """
    if isinstance(s, float):
        return round(s, 2)
    if s == '':
        return 0.0
    try:
        return int(s)
    except ValueError:
        return float(s)


def get_color(i):
    """
    Gets a hex color from list.

    :param i: index of array
    :return: Returns a hex color
    """
    colors = ['#F7464A', '#46BFBD', '#C0C0C0', '#3E5DE0',
              '#db518b', '#5cd08c', '#c1812c', '#1b69a1']
    if i >= len(colors):
        i = 0
    return colors[i]


def get_hightlight_color(i):
    """
    Gets a hex color from list.

    :param i: index of array
    :return: Returns a hex color
    """
    colors = ['#FF5A5E', '#5AD3D1', '#D8D8D8', '#3F5EDF',
              '#db5f93', '#73d099', '#bf8e4c', '#3376a6']
    if i >= len(colors):
        i = 0
    return colors[i]
