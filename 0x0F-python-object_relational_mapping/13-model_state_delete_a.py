#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
            )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    state_to_delete = session.query(State).filter(State.name.like(f"%a%")).all()

    for state in state_to_delete:
        session.delete(state)
    session.commit()

    session.close()
