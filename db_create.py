#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    db_create.py
    ---------------

    Run this script to automatically create the tables from db_schema.sql
"""

from app.db import connect_db


def run_sql_file(filename, conn):
    """
    The function takes a filename and a connection as inputs
    and will run the SQL query on the given connection.
    """

    file = open(filename, 'r')
    sql = " ".join(file.readlines())
    print("\n" + "Start executing: " + filename + "\n")
    print(sql)
    cur = conn.cursor()
    cur.execute(sql)
    print("Finished executing: " + filename + "\n")


def main():
    connection = connect_db()
    run_sql_file("db_schema.sql", connection)
    connection.close()


if __name__ == "__main__":
    main()
