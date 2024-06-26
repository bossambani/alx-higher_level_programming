#!/usr/bin/python3
"""
script that lists all State objects that contain the letter a from
the database hbtn_0e_6_usa
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

    states = session.query(State).filter(State.name.like(
        f'%a%')).order_by(State.id.asc()).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
