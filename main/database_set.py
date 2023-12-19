import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = f"postgresql://postgres:1111@localhost:5432/testdb"

database = databases.Database(DATABASE_URL)

Base = declarative_base()
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
