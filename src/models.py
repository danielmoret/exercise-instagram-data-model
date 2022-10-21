import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    phone = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    create_at = Column(DateTime)
    

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    text = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    type_post_id = Column(Integer, ForeignKey('type_post.id'))
    post_shared_id = Column(Integer, ForeignKey('post.id'))

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(250))
    date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Follow(Base):
    __tablename__ = 'follow'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

class TypePost(Base):
    __tablename__ = 'type_post'
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')