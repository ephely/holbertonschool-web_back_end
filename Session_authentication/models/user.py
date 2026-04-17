#!/usr/bin/env python3
"""
User model
"""
from models.base import Base


class User(Base):
    """ User class
    """

    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize a User instance
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')

    def display_name(self) -> str:
        """ Display name
        """
        if self.email is None and \
           self.first_name is None and \
           self.last_name is None:
            return ""
        if self.first_name is None and self.last_name is None:
            return f"{self.email}"
        if self.last_name is None:
            return f"{self.first_name}"
        if self.first_name is None:
            return f"{self.last_name}"
        return f"{self.first_name} {self.last_name}"

    def is_valid_password(self, pwd: str) -> bool:
        """ Validate password """
        if pwd is None or type(pwd) is not str:
            return False
        if self.password is None:
            return False
        import hashlib
        return self.password == hashlib.md5(pwd.encode()).hexdigest().lower() or self.password == pwd

    def to_json(self, for_serialization: bool = False) -> dict:
        """ Convert the object a JSON dictionary with password removal
        """
        user_dict = super().to_json(for_serialization)
        if not for_serialization and 'password' in user_dict:
            del user_dict['password']
        return user_dict
