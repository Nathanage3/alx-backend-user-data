#!/usr/bin/env python3

import bcrypt
from uuid import uuid4
from typing import Union
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
  """Hashes a password"""
  hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
  return hashed_pwd

class Auth:
  """Auth class to interact with authentication db.
  """

  def __init__(self):
    self._db = DB()

  def register_user(self, email: str, password: str) -> User:
    """Adds a new user too the database.
    """
    try:
      self._db.find_user_by(email=email)
    except NoResultFound:
      return self._db.add_user(email, _hash_password(password))
    raise ValueError("User {} already exists".format(email))


