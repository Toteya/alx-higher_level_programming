#!/usr/bin/python3
"""
Module 1-filter_states
Connects to and queries a db
"""

import MySQLdb
import sys


def main():
    """ main function: connects to and queries the db as provided by the
    command-line arguments
    """
    my_host = "localhost"
    my_port = 3306
    my_user = sys.argv[1]
    my_pass = sys.argv[2]
    my_database = sys.argv[3]

    db = MySQLdb.connect(host=my_host, user=my_user,
                         passwd=my_pass, db=my_database, port=my_port)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
