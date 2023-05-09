#!/usr/bin/env python3
"""Improved version of 12-log_stats.py.
Added the top 10 of the most present IPs in the collection nginx
of the database logs
"""
from pymongo import MongoClient

if __name__ == "__main__":
    """Provides stats about the Nginx logs stored in a MongoDB
    with the most present IPs
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Get number of documents in this collection
    print(f"{collection.estimated_document_count()} logs")

    # Get number of documents with each HTTP method
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_doc_count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_doc_count}")

    # Get number of documents with method=GET and path=/status
    status_count = collection.count_documents(
        {'method': 'GET', 'path': "/status"})
    print(f"{status_count} status check")
    
    # Get most present IPs
    
    ip_list = collection.aggregate([
        {
            "$group":
                {
                    "_id": "$ip",
                    "count": {"$sum": 1}
                }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 10
        },
        {
            "$project": {
                "_id": 0,
                "ip": "$_id",
                "count": 1
            }
        }
    ])
    print("IPs:")
    for ip in ip_list:
        print(f"\t{ip.get('ip')}: {ip.get('count')}")
