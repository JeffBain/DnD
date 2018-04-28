from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # Set up test data for now
    from inventory.models import Item, Inventory, ItemInventoryMap
    print ("Iniatlizing Database")
    Base.metadata.create_all(bind=engine)

    dagger = Item(name='dagger')
    db_session.add(dagger)
    rapier = Item(name='rapier')
    db_session.add(rapier)
    db_session.commit()

