#!/usr/bin/env python3
"""Write a Python script that provides some
stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log_stats():
    """
    Gives stats about Nginx logs database
    """
    collection = MongoClient().logs.nginx
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status_check = collection.count_documents({"method":
                                               "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
