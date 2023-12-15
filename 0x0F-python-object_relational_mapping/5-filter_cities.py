#!/usr/bin/python3
"""Module that lists cities of a state passed as argv[4]"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("\
            SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states\
            ON cities.state_id = states.id;\
            ")

    rows = cur.fetchall()
    my_list = []
    for row in rows:
        if (row[2] == argv[4]):
            my_list.append(row[1])
    print(", ".join(my_list))

    cur.close()
    db.close()
