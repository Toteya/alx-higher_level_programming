#!/usr/bin/python3
"""
Module model_state_fetch_all
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, select, MetaData
import urllib


def main():
    """
    Connects to and queries the given database
    Lists all State objects
    """
    user = sys.argv[1]
    password = urllib.parse.quote_plus(sys.argv[2])
    database = sys.argv[3]
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                                                         password,
                                                         database)
    engine = create_engine(db_url, pool_pre_ping=True)
    # Base.metadata.create_all(engine)

    session = engine.connect()
    result = session.execute(select(State).where(State.id == 1))

    result = list(result)
    print('{}: {}'.format(result[0].id, result[0].name))


if __name__ == '__main__':
    main()
