#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    db_create.py
    ---------------

    Run this script to automatically create your tables from db_schema.sql

"""


from app.db import connect_db


def run_sql_file(filename, connection):
    """
    The function takes a filename and a connection as inputs
    and will run the SQL query on the given connection
    """

    file = open(filename, 'r')
    sql = " ".join(file.readlines())
    print("Start executing: " + filename + "\n" + sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    print("Finished executing.")


def main():
    connection = connect_db()
    run_sql_file("db_schema.sql", connection)
    connection.close()


if __name__ == "__main__":
    main()
