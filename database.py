from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

ENGINE = create_engine('postgresql://postgres:2160607@localhost/fast_3', echo=True)
Base = declarative_base()
session = sessionmaker()
