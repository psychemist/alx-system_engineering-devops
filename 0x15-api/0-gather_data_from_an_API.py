#!/usr/bin/python3
"""Queries a REST API using a request for a given employee ID
and returns information about their TODO list progress
"""
from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/todos/{}".
                     format(argv[1]))

    for todo in r.json():
        # print("".format(todo.get('id'), todo.userId, todo.title, todo.completed))
