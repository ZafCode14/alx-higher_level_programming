#!/usr/bin/python3
"""Module with a script that lists states with letter 'N'."""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("\
            SELECT * FROM states\
            WHERE name LIKE 'N%';\
            ")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
