#!/usr/bin/python3
"""
Module 5-filter_cities
Connects to and queries a db
"""

import MySQLdb
import sys


def main():
    """ connects to and queries the db as provided by the
    command-line arguments
    Lists all cities from the state as specified by the use from the given
    database
    """
    my_host = "localhost"
    my_port = 3306
    my_user = sys.argv[1]
    my_pass = sys.argv[2]
    my_database = sys.argv[3]
    my_state = sys.argv[4]

    if ';' in my_state:
        return

    db = MySQLdb.connect(host=my_host, user=my_user,
                         passwd=my_pass, db=my_database, port=my_port)
    cur = db.cursor()
    query = "".join(["SELECT cities.name ",
                     "FROM cities, states ",
                     "WHERE cities.state_id = states.id ",
                     "AND states.name = '{}' ".format(my_state),
                     "ORDER BY cities.id ASC;"])
    cur.execute(query)
    rows = cur.fetchall()
    result = ""
    for row in rows:
        result += row[0] + ', '
    result = result.strip().strip(',')
    print(result)


if __name__ == '__main__':
    main()
