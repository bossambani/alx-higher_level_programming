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

    state_to_update = session.query(State).filter_by(id=2).first()
    state_to_update.name = 'New Mexico'
    session.commit()

    session.close()
