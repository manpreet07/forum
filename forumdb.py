
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class Forum(Base):
    __tablename__ = 'forum'

    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    time = Column(DateTime, default=datetime.datetime.utcnow)

engine = create_engine('sqlite:///forum.db')

Base.metadata.create_all(engine)