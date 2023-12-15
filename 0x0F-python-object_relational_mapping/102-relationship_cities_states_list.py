#!/usr/bin/python3
"""Module that lists all State and corresponding City"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    conn_str = "mysql://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(conn_str, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    for state in states:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
