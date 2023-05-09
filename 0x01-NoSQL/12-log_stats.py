#!/usr/bin/env python3
"""A Python script that provides some stats about Nginx logs"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Provides stats about the Nginx logs stored in a MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print(f"{collection.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_doc_count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_doc_count}")

    status_count = collection.count_documents(
        {'method': 'GET', 'path': "/status"})
    print(f"{status_count} status check")
