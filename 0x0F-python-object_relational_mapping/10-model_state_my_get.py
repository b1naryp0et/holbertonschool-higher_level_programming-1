#!/usr/bin/python3
# list all states
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    squery = session.query(State).filter(State.name == sys.argv[4]).first()

    if squery is None:
        print("Not found")
    else:
        print(squery.id)

    session.close()
