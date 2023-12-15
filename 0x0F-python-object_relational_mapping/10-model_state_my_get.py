#!/usr/bin/python3
"""Module that prints the State the name passed in argv[4]"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    conn_str = "mysql://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(conn_str, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()

    found = False
    for state in states:
        if argv[4] == state.name:
            print("{}".format(state.id))
            found = True

    if (not found):
        print("Not found");
