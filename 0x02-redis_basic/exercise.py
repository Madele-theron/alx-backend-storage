#!/usr/bin/env python3
""" Redis task solutions"""
import redis
from typing import Union
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
