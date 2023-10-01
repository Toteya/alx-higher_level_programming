#!/usr/bin/python3
"""
Module 9-model_state_filter_a
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib


def main():
    """
    Connects to and queries the given database
    Lists all State objects containing 'a'
    """
    user = sys.argv[1]
    password = urllib.parse.quote_plus(sys.argv[2])
    database = sys.argv[3]
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                                                         password,
                                                         database)
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        result = session.query(State).order_by(State.id).filter(State.name.contains('a'))
        # print(type(result))
        for item in result:
            print('{}: {}'.format(item.id, item.name))


if __name__ == '__main__':
    main()
