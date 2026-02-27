#!/usr/bin/env python3
"""
Base model
"""
from datetime import datetime
from typing import TypeVar, List, Iterable
from uuid import uuid4
import json
import os


TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S"
DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../db"
DATA = {}


class Base():
    """ Base class
    """

    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize a Base instance
        """
        s_class = self.__class__.__name__
        if DATA.get(s_class) is None:
            DATA[s_class] = {}

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        value, TIMESTAMP_FORMAT)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        DATA[s_class][self.id] = self

    def __eq__(self, other: TypeVar("Base")) -> bool:
        """ Equality
        """
        if type(self) != type(other):
            return False
        if not isinstance(self, Base) or not isinstance(other, Base):
            return False
        return self.id == other.id

    def to_json(self, for_serialization: bool = False) -> dict:
        """ Convert the object a JSON dictionary
        """
        result = {}
        for key, value in self.__dict__.items():
            if not for_serialization and key.startswith("_"):
                continue
            if type(value) is datetime:
                result[key] = value.strftime(TIMESTAMP_FORMAT)
            else:
                result[key] = value
        return result

    @classmethod
    def load_from_file(cls):
        """ Load all objects from file
        """
        s_class = cls.__name__
        file_path = f"{DATA_DIR}/{s_class}.json"
        if not os.path.exists(file_path):
            return

        with open(file_path, 'r') as f:
            objs_json = json.load(f)
            for obj_id, obj_json in objs_json.items():
                cls(**obj_json)

    @classmethod
    def all(cls) -> Iterable[TypeVar("Base")]:
        """ All objects
        """
        return DATA[cls.__name__].values()

    def save(self):
        """ Save object to file
        """
        s_class = self.__class__.__name__
        DATA[s_class][self.id] = self
        file_path = f"{DATA_DIR}/{s_class}.json"
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        objs_json = {}
        for obj_id, obj in DATA[s_class].items():
            objs_json[obj_id] = obj.to_json(True)

        with open(file_path, 'w') as f:
            json.dump(objs_json, f)

    def remove(self):
        """ Remove object from file
        """
        s_class = self.__class__.__name__
        file_path = f"{DATA_DIR}/{s_class}.json"
        if not os.path.exists(file_path):
            return

        objs_json = {}
        with open(file_path, 'r') as f:
            objs_json = json.load(f)

        if self.id in objs_json:
            del objs_json[self.id]
            with open(file_path, 'w') as f:
                json.dump(objs_json, f)

    @classmethod
    def count(cls) -> int:
        """ Count all objects
        """
        return len(cls.all())

    @classmethod
    def get(cls, id: str) -> TypeVar("Base"):
        """ Get object by ID
        """
        all_objs = cls.all()
        for obj in all_objs:
            if obj.id == id:
                return obj
        return None

    @classmethod
    def search(cls, attributes: dict = {}) -> List[TypeVar("Base")]:
        """ Search object with attributes
        """
        all_objs = cls.all()
        if not attributes:
            return all_objs

        result = []
        for obj in all_objs:
            match = True
            for key, value in attributes.items():
                if getattr(obj, key) != value:
                    match = False
                    break
            if match:
                result.append(obj)
        return result
