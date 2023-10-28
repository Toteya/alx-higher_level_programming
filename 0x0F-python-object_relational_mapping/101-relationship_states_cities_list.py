#!/usr/bin/python3
"""
module 101-relationship_states_cities_list
Lists all the State objects and the corresponding City objects contained
in the given database
"""
from relationship_city import City
from relationship_state import State
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    password = quote(sys.argv[2])
    database = sys.argv[3]
    db_url = 'mysql+mysqldb://%s:%s@localhost/%s' % (user,
                                                     password,
                                                     database)
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        result = session.query(State).options(joinedload(State.cities)).all()
        for state in result:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("\t{}: {}".format(city.id, city.name))
