#!/usr/bin/env python3
"""
Basic Cache class
"""

import redis
import uuid
from typing import Union


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
