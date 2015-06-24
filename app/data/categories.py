# -*- coding: utf-8 -*-

"""
    categories.py
    ~~~~~~~~~~~~

    This module implements the methods for CRUD content to the categories table.
"""

from app.db import get_cursor


# Get category_list for a given project_id
def get_category_list(cur, project_id):
    cur.execute('''
        SELECT category_id, category_name, project_id
        FROM categories
        WHERE project_id = %s
    ''', (project_id,))

    category_list = []
    for (category_id, category_name, project_id) in cur:
        cur2 = get_cursor()
        cur2.execute('''
            SELECT item_id, item_name, description, budget, actual, notes, category_id
            FROM items
            WHERE category_id = %s
        ''', (category_id,))

        item_list = []
        for (item_id, item_name, description, budget, actual, notes, category_id) in cur2:
            item_list.append({
                'item_id':     item_id,
                'item_name':   item_name,
                'description': description,
                'budget':      budget,
                'actual':      actual,
                'notes':       notes,
                'category_id': category_id,
            })

        category_list.append({
            'category_id':   category_id,
            'category_name': category_name,
            'item_list':     item_list,
            'project_id':    project_id
        })
    return category_list


# Get category_id for a given category and project_id
def get_category_id(cur, category_name, project_id):
    cur.execute('''
        SELECT category_id
        FROM categories
        WHERE category_name = %s
        AND project_id = %s
    ''', (category_name, project_id))

    (category_id,) = cur.fetchone()
    if category_id is not None:
        return category_id
