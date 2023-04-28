#!/usr/bin/python3
"""Queries a REST API using a request for a given employee ID
and returns information about their TODO list progress
"""
import requests
from sys import argv

if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/".
    users = requests.get("https://jsonplaceholder.typicode.com/users/}".

    for todo in r.json():
        # print("".format(todo.get('id'), todo.userId, todo.title, todo.completed))
