#!/usr/bin/env python3
"""A Python script that provides some stats about Nginx logs
stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Provides stats about the Nginx logs stored in a MongoDB"""
    # Connect to MongoDB:
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Get number of documents in this collection:
    # `x logs` where `x` is the number of documents in this collection
    print(f"{collection.count_documents()} logs")

    # Get number of documents with each HTTP method:
    # Methods:
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_doc_count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_doc_count}")

    # Get number of documents with method=GET and path=/status
    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_count} status check")
