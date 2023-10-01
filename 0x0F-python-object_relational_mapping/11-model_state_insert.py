#!/usr/bin/python3
"""
Module 11-model_state_insert
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote


def main():
    """
    Connects to and queries the given database
    Adds a new State 'Louisiana' to the table
    """
    user = sys.argv[1]
    password = quote(sys.argv[2])
    database = sys.argv[3]
    db_url = 'mysql+mysqldb://%s:%s@localhost/%s' % (user,
                                                     password,
                                                     database)
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    new_state = State(name='Louisiana')
    with Session() as session:
        session.add(new_state)
        session.commit()
        print(new_state.id)


if __name__ == '__main__':
    main()
