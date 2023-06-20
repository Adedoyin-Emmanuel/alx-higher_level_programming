#!/usr/bin/python3
'''
A script that prints the first State object from
the database hbtn_0e_6_usa
'''
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State


if __name__ == '__main__':
    dbEngine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    InstanceSession = sessionmaker(bind=dbEngine)
    session = InstanceSession()

    state = session.query(State).order_by(State.id).first()
    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')
    session.close()
