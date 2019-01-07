from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'mysql+pymysql://root:88Canapozzo88@localhost/fake_news_db')
Base = declarative_base()


class Links(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    link_domain = Column(String)
    name_domain = Column(String)
    deleted = Column(Integer)


class Searched_links(Base):
    __tablename__ = 'searched_links'

    id = Column(Integer, primary_key=True)
    id_link_domain = Column(Integer)
    link_searched = Column(String)
    n_search = Column(Integer)
    n_positive = Column(Integer)
