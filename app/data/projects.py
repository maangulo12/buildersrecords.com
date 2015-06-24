# -*- coding: utf-8 -*-

"""
    projects.py
    ~~~~~~~~~~~~

    This module implements the methods for CRUD content to the projects table.
"""

from app.data.categories import get_category_id


# Get project_list for a given user
def get_project_list(cur, user_id):
    cur.execute('''
        SELECT project_id, project_name, project_type
        FROM projects
        WHERE user_id = %s
    ''', (user_id,))

    project_list = []
    for (project_id, project_name, project_type) in cur:
        project_list.append({
            'project_id':   project_id,
            'project_name': project_name,
            'project_type': project_type,
        })
    return project_list


# Delete a specific project for a given user
def remove_project(cur, user_id, project_id):
    cur.execute('''
        DELETE FROM projects
        WHERE user_id = %s
        AND project_id = %s
    ''', (user_id, project_id))


# Check if project_id exists
def project_id_exists(cur, project_id):
    cur.execute('''
        SELECT COUNT(project_id)
        FROM projects
        WHERE project_id = %s
    ''', (project_id,))

    (count,) = cur.fetchone()
    if count == 1:
        return True


# Get project_detail for a given project_id
def get_project_detail(cur, project_id):
    cur.execute('''
        SELECT *
        FROM projects
        WHERE project_id = %s
    ''', (project_id,))

    for (project_id, project_name, project_type, user_id) in cur:
        project_detail = {
            'project_id':   project_id,
            'project_name': project_name,
            'project_type': project_type,
            'user_id':      user_id
        }
        return project_detail


# Check if project name exists
def project_name_exists(cur, project_name, user_id):
    cur.execute('''
        SELECT COUNT(project_name)
        FROM projects
        WHERE project_name = %s
        AND user_id = %s
    ''', (project_name, user_id))

    (count,) = cur.fetchone()
    if count == 1:
        return True

# Get project_id for a given project and user_id
def get_project_id(cur, project_name, user_id):
    cur.execute('''
        SELECT project_id
        FROM projects
        WHERE project_name = %s
        AND user_id = %s
    ''', (project_name, user_id))

    (project_id,) = cur.fetchone()
    if project_id is not None:
        return project_id


# Creates a project
def create_project(cur, project_name, project_type, categories, user_id):
    cur.execute('''
        INSERT INTO projects (project_name, project_type, user_id)
        VALUES (%s, %s, %s);
    ''', (project_name, project_type, user_id))

    project_id = get_project_id(cur, project_name, user_id)

    for category in categories:
        cur.execute('''
            INSERT INTO categories (category_name, project_id)
            VALUES (%s, %s);
        ''', (category['category_name'],
              project_id))

        category_id = get_category_id(cur, category['category_name'], project_id)

        for item in category['item_list']:
            cur.execute('''
                INSERT INTO items (item_name, description, budget, actual, notes, category_id)
                VALUES (%s, %s, %s, %s, %s, %s);
            ''', (item['cost_category'],
                  item['notes'],
                  item['budget'],
                  item['actual'],
                  item['explanations'],
                  category_id))
