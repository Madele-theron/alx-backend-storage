#!/usr/bin/env python3
"""A Python function that returns all students sorted by average score:
"""

def top_students(mongo_collection):
    """ List all students sorted by score """
    return mongo_collection.aggregate([
        {
            '$project': {
                'name': '$name',
                'averageScore': {
                    '$avg': "$topics.score"
                }
            }
        },
        {
            '$sort': {
                "averageScore": -1
            }
        }
    ])
def top_students(mongo_collection):
    """List all students sorted by their average score

    Args:
        mongo_collection (pymongo collection object): MongoDB collection

    Returns:
        All students sorted by average score
    """

    student_list = mongo_collection.aggregated([
        {
            '$projects': {
                'name': '$name',
                'averageScore': {'$avg': "$topics.score"}
            }
        },
        {
            '$sort': {"averageScore": -1}
        }
    ])
    
    return student_list
