import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)
    picture = Column(String(250))

class ReadingList(Base):
    __tablename__ = 'reading_list'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id'            : self.id,
            'name'          : self.name,
            'description'   : self.description,
        }

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    category = Column(String(80))
    author_first_name = Column(String(80))
    author_last_name = Column(String(80))
    description = Column(String)
    website = Column(String)
    reading_list_id = Column(Integer, ForeignKey('reading_list.id'))
    reading_list = relationship(ReadingList)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id'                : self.id,
            'name'              : self.name,
            'category'          : self.category,
            'author_first_name' : self.author_first_name,
            'author_last_name'  : self.author_last_name,
            'description'       : self.description,
            'website'           : self.website,
        }

engine = create_engine('sqlite:///readinglistwithusers.db')
Base.metadata.create_all(engine)