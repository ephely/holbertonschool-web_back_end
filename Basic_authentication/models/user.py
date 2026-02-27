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
