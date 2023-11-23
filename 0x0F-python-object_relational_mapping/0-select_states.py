#!/usr/bin/python3

"""
Script that lists all states from
Database `hbtn_0e_0_usa`
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database
    """

    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            port=3306,
            passwd=argv[2],
            db=argv[3]
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)