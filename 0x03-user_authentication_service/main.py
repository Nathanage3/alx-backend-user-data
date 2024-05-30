#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from auth import Auth
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

my_db = DB()
AUTH = Auth()

email = "test@gmail.com"
user = my_db.add_user(email, "PwdHashed")
#print(user.email)
session_id = AUTH.create_session(email)
user.session_id = session_id
my_db._session.commit()

found_user = AUTH.get_user_from_session_id(session_id)
if found_user:
  print(found_user.id)
else:
  print("Not Found")
  