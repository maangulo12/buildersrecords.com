# -*- coding: utf-8 -*-

"""
    users.py
    ~~~~~~~~~~~~

    This module implements the methods for CRUD content for the projects table.
"""

# Get project_list for a given user
def get_project_list(cur, user_id):
    cur.execute('''
        SELECT project_id, project_name, project_type, address, city, state, zipcode, project_cost
        FROM projects
        WHERE user_id = %s
    ''', (user_id,))

    project_list = []
    for (project_id, project_name, project_type, address, city, state, zipcode, project_cost) in cur:
        project_list.append({
            'project_id': project_id,
            'project_name': project_name,
            'project_type': project_type,
            'address': address,
            'city': city,
            'state': state,
            'zipcode': zipcode,
            'project_cost': project_cost
        })
    return project_list
