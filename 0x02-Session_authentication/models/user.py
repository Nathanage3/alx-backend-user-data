#!/usr/bin/env python3
"""User module.
"""
import hashlib
import bcrypt
from models.base import Base


class User(Base):
    """User class.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """Initialize a User instance.
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email')
        self._password = kwargs.get('_password')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')

    @property
    def password(self) -> str:
        """Getter of the password.
        """
        return self._password

    @password.setter
    def password(self, pwd: str):
        """Setter of a new password: encrypt in SHA256.

        WARNING: Use a better password hashing algorithm like argon2
        or bcrypt in real-world projects.
        """
        if pwd is None or type(pwd) is not str:
            self._password = None
        else:
            hashed = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())
            self.__password = hashed.decode('utf-8')

    def is_valid_password(self, pwd: str) -> bool:
        """Validate a password.
        """
        if pwd is None or type(pwd) is not str:
            return False
        if self.password is None:
            return False
        
        return bcrypt.checkpw(pwd.encode('utf-8'), self.password.encode('utf-8'))

    def display_name(self) -> str:
        """Display User name based on email/first_name/last_name.
        """
        if self.email is None and self.first_name is None \
                and self.last_name is None:
            return ""
        if self.first_name is None and self.last_name is None:
            return "{}".format(self.email)
        if self.last_name is None:
            return "{}".format(self.first_name)
        if self.first_name is None:
            return "{}".format(self.last_name)
        else:
            return "{} {}".format(self.first_name, self.last_name)