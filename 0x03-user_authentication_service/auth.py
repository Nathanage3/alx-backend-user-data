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

def _generate_uuid() -> str:
  """Generate UUID.
  """
  return str(uuid4())


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



  def valid_login(self, email: str, password: str) -> bool:
    """A valid login credentials.
    """
    user = None
    try:
      user = self._db.find_user_by(email=email)
      if user is not None:
        return bcrypt.checkpw(password.encode("utf-8"),
                              user.hashed_password,
        )
    except NoResultFound:
      return False
    return False

  def create_session(self, email: str) -> str:
    """Create a new session for a user.
    """
    user = None
    try:
      user = self._db.find_user_by(email=email)
    except NoResultFound:
      return None
    if user is None:
      return None
    session_id = _generate_uuid()
    self._db.update_user(user.id, session_id=session_id)
    return session_id

  def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Retrieves a user based on a given session ID.
        """
        user = None
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user
  
  def destroy_session(self, user_id: int) -> None:
        """Destroys a session associated with a given user.
        """
        if user_id is None:
            return None
        self._db.update_user(user_id, session_id=None)


