#!/usr/bin/env python3
"""
Basic Cache class
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Cache class using Redis"""

    def __init__(self):
        """Initialize Redis client and flush database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a random key

        Returns:
            The generated key as a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None]:
        """
        Get data from Redis and recover original type

        Returns:
            The data in original type, or None if key does not exist
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Get data from Redis and return as a string
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Get data from Redis and return as an int
        """
        return self.get(key, fn=int)
