#!/usr/bin/env python3
""" Redis task solutions"""
import redis
from typing import Union, Callable, Optional
from uuid import uuid4


class Cache:
    """ Writing strings to Redis """
    def __init__(self):
        """Instance of the Redis client as a private variable """
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate random key and store input data in Redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Convert the data back to the desired format"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Auto parametrize Cache.get with correct conversion function."""
        data = self._redis.get(key)
        return data.decode('utf-8')

    def get_int(self, key: str) -> int:
        """Auto parametrize Cache.get with correct conversion function."""
        data = self._redis.get(key)
        return data.get(key, int)
