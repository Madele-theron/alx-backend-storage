#!/usr/bin/env python3
""" Redis task solutions"""
import redis
from typing import Union, Callable, Optional
from functools import wraps
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """Decorator that returns a callable"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increments count for the key every time the method is called"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator that returns a callable"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Store the history of inputs and outputs for a particular function"""
        key_input = method.__qualname__ + ':inputs'
        key_output = method.__qualname__ + ':outputs'

        input_data: str = str(args)
        self._redis.rpush(key_input, input_data)

        output_data: str(method(self, *args, **kwargs))
        self._redis.rpush(key_output, output_data)

        return output_data

    return wrapper


class Cache:
    """ Writing strings to Redis """
    def __init__(self):
        """Instance of the Redis client as a private variable """
        self._redis = redis.Redis()
        self._redis.flushdb

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate random key and store input data in Redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
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
