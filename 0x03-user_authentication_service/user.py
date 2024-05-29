#!/usr/bin/env python3
"""User module"""

import sqlalchemy
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Base = declarative_base()


class User(Base):
    """Representation of user"""
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=False)
