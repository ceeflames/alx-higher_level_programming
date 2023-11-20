#!/usr/bin/python3
"""
Script that takes in argument and
displays all values in the states
table of hbtn_oe_0_usa where name
matches the argument.

This time, It is safe from MySQL injections.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    """

    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            port=3306,
            passwd=argv[2],
            db=argv[3]
            )

    with db.cursor() as cur:
        cur.execute("""
        SELECT *
        FROM
            states
        WHERE
            name LIKE BINARY %(name)s
        ORDER BY
        states.id ASC
        """, {
                'name': argv[4]
                    })
        rows = cur.fetchall()
        if rows is None:
            for row in rows:
                print(row)
