#!/usr/bin/env python3
"""A Python function that lists all documents in a collection:
"""


def list_all(mongo_collection):
    """A Python function that lists all documents in a collection

    Args:
        mongo_collection (pymongo.collection.Collection): MongoDB collection

    Returns:
        List of all documents in collection
        or an empty list if there's no document in the collection
    """
    documents = list(mongo_collection.find())
    return documents
