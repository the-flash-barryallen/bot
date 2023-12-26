import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from data.config import env

DATABASE_URL = f"postgresql://DB_HOST:DB_PASS@DB_HOST:DB_PORT/DB_NAME"

database = databases.Database(DATABASE_URL)

DB_USER = env.str("DB_USER")
DB_NAME = env.str("DB_NAME")
DB_PASS = env.str("DB_PASS")
DB_HOST = env.str("DB_HOST")
DB_PORT = env.str("DB_PORT")

Base = declarative_base()
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
