#!/usr/bin/env python3
""" Redis advance task solutions"""
import redis
import requests

client = redis.Redis()
count = 0

def get_page(url: str) -> str:
    """
    Track how many times a particular URL was accessed in the key
    Cache the result with an expiration time of 10 seconds.
    """
    client.set(f"cached:{url}", count)

    # Get data response
    response = requests.get(url)

    # Increment count for URL
    client.incr(f"count:{url}")
    data = client.get(f"cached:{url}")
    client.setex(f"cached:{url}", 10, data)

    return response.text
