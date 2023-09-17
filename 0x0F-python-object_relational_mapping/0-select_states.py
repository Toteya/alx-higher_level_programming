#!/usr/bin/python3

import MySQLdb
import sys


def main():
    my_host = "localhost"
    my_user = sys.argv[1]
    my_pass = sys.argv[2]
    my_database = sys.argv[3]

    db = MySQLdb.connect(host=my_host, user=my_user,
                         passwd=my_pass, db=my_database)
    cur = db.cursor()
    cur.execute("SELECT * FROM hbtn_0e_0_usa.states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
