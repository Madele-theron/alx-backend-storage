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
        Id of new document
    """
    
    document = mongo_collection.insert(kwargs)
    return document.inserted_id
