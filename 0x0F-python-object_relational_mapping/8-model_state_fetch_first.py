#!/usr/bin/python3
"""Module that prints the first state"""
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

    if (states):
        print("{}: {}".format(states[0].id, states[0].name))
    else:
        print("Nothing")
