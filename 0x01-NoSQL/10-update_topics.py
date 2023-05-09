#!/usr/bin/env python3
"""A Python function that changes all topics of a
school document based on the name:
"""


def update_topics(mongo_collection, name, topics):
    """Updates the topics field of all school documents in the
    specified collection with the given name.

    Args:
        mongo_collection (pymongo collection object): MongoDB collection
        name (str): the school name to update
        topics (list of strings): the list of topics approached in the

    Returns:
        New document
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}},
    )
