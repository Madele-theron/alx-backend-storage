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
                    
                }
        }
    ])
    print("IPs:")
    

    print("IPs:")
    top_ips = collection.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])
    for ip in top_ips:
        print(f"\t{ip.get('ip')}: {ip.get('count')}")


# IPs:
#     172.31.63.67: 15805
#     172.31.2.14: 15805
#     172.31.29.194: 15805
#     69.162.124.230: 529
#     64.124.26.109: 408
#     64.62.224.29: 217
#     34.207.121.61: 183
#     47.88.100.4: 166
#     45.249.84.250: 160
#     216.244.66.228: 150