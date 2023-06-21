from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql+psycopg2://kaznuuser:mk gkmt gkjt@localhost/kaznudb'
#DATABASE_URL = 'postgresql+psycopg2://kaznuuser:komtkgm@185.4.180.217/kaznudb'

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

