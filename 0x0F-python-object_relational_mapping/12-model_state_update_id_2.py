#!/usr/bin/python3
"""
Module 12-model_state_update_id_2
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote


def main():
    """
    Connects to and queries the given database
    Updates the name of a State whose id is 2
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
        with session.begin():
            session.query(State).filter(State.id == 2).update(
                    {
                        'name': 'New Mexico'
                    },
                    synchronize_session='fetch'
                )
            session.commit()


if __name__ == '__main__':
    main()
