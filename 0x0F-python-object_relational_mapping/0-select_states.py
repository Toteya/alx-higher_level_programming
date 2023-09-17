#!/usr/bin/python3

import MySQLdb
import sys


def main():
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect("localhost", user, password, database)
    cur = db.cursor()
    cur.execute("SELECT * FROM hbtn_0e_0_usa.states")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
