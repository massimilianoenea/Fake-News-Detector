import Model.Links as dbEntity
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=dbEntity.engine)
session = Session()

links = dbEntity.Links(link_domain = 'prova_link_domain2', name_domain = 'prova_name_domain2', deleted = 0)
session.add(links)
session.commit()