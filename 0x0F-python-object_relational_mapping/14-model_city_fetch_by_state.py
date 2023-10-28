#!/usr/bin/python3
"""
module 14-model_city_fetch_by_state
Prints all City objects from the given database
"""

from model_city import City
from model_state import State
from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
        query = session.query(City, State).order_by(City.id)
        result = query.filter(State.id == City.state_id).all()
        for c, s in result:
            print("{}: ({}) {}".format(s.name, c.id, c.name))
