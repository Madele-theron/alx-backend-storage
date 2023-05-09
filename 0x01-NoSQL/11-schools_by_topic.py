#!/usr/bin/env python3
"""A Python function that returns the list of schools with a specific topic:
"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools with a specific topic

    Args:
        mongo_collection (pymongo collection object): MongoDB collection
        topic (str): the topic searched

    Returns:
        A list of schools having a specific topic:
    """
    schools = mongo_collection.find({"topics": topic})
    return schools

