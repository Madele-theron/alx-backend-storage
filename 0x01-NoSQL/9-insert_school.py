#!/usr/bin/env python3
"""A Python function that inserts a new document in
a collection based on kwargs:
"""


def insert_school(mongo_collection, **kwargs):
    """A Python function that inserts a document in a collection

    Args:
        mongo_collection (pymongo.collection.Collection): MongoDB collection
        **kwargs: The keyword arguments for the new document.

    Returns:
        New document
    """
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
