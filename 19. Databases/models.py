from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from zope.sqlalchemy import register

# 1. Setup Mesin Database
# Scoped session memastikan setiap request punya koneksi sendiri
DBSession = scoped_session(sessionmaker())
register(DBSession) # Sambungkan ke Transaction Manager (pyramid_tm)

Base = declarative_base()

# 2. Definisi Tabel 'Page'
class Page(Base):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    body = Column(Text)

# Fungsi helper untuk mengambil session database dari request
def get_tm_session(session_factory, transaction_manager):
    dbsession = session_factory()
    dbsession.transaction_manager = transaction_manager
    return dbsession