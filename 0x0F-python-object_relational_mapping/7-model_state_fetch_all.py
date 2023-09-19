#!/usr/bin/python3
"""
Module model_state_fetch_all
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, select, MetaData


def main():
    """
    Connects to and queries the given database
    Lists all State objects
    """
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    # Base.metadata.create_all(engine)

    session = engine.connect()
    result = session.execute(select(State).order_by(State.id))

    for row in result:
        print('{}: {}'.format(row.id, row.name))


if __name__ == '__main__':
    main()
