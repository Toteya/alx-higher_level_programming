#!/usr/bin/python3
"""
Module 10-model_state_my_get
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib


def main():
    """
    Connects to and queries the given database
    Prints a State object that matches the name passes as parameter
    """
    user = sys.argv[1]
    password = urllib.parse.quote_plus(sys.argv[2])
    database = sys.argv[3]
    name = sys.argv[4]
    db_url = 'mysql+mysqldb://%s:%s@localhost/%s' % (user,
                                                     password,
                                                     database)
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        result = session.query(State).filter(State.name == name).first()
        if not result:
            print("Not found")
        else:
            print(result.id)


if __name__ == '__main__':
    main()
