from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:88Canapozzo88@localhost/fake_news_db')
Base = declarative_base()

def getEngine():
    return engine

def getBase():
    return Base