#!/usr/bin/python3
"""
Module 4-cities_by_state
Connects to and queries a db
"""

import MySQLdb
import sys


def main():
    """ connects to and queries the db as provided by the
    command-line arguments
    Lists all cities from the given database
    """
    my_host = "localhost"
    my_port = 3306
    my_user = sys.argv[1]
    my_pass = sys.argv[2]
    my_database = sys.argv[3]

    db = MySQLdb.connect(host=my_host, user=my_user,
                         passwd=my_pass, db=my_database, port=my_port)
    cur = db.cursor()
    query = "".join(["SELECT cities.id, cities.name, states.name ",
                     "FROM cities, states ",
                     "WHERE cities.state_id = states.id ",
                     "ORDER BY cities.id ASC;"])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
