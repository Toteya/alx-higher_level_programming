#!/usr/bin/python3
"""
module 100-relationship_state_cities.py
Creates the State 'California' with the City 'San Fransisco' from the
given database
"""
from relationship_city import City
from relationship_state import Base, State
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
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    my_city = City(name="San Francisco")
    my_state = State(name='California', cities=[my_city])

    with Session() as session:
        session.add(my_state)
        session.add(my_city)
        session.commit()
