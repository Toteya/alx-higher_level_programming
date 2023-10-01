#!/usr/bin/python3
"""
Module 13-model_state_delete_a.py
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote


def main():
    """
    Connects to and queries the given database
    Deletes all State objects containing 'a'
    """
    user = sys.argv[1]
    password = quote(sys.argv[2])
    database = sys.argv[3]
    db_url = 'mysql+mysqldb://%s:%s@localhost/%s' % (user,
                                                     password,
                                                     database)
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        result = session.query(State).filter(State.name.contains('a'))
        for obj in result:
            session.delete(obj)
        session.commit()


if __name__ == '__main__':
    main()
