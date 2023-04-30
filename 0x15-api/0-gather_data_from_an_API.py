#!/usr/bin/python3
"""Queries a REST API using a request for a given employee ID
and returns information about their TODO list progress
"""
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(argv[1]))
    todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos/"
                         .format(argv[1]))

    name = (user.json().get('name'))
    task_done = task_todo = 0

    for todo in todos.json():
        if todo.get('completed') is True:
            task_done += 1
        else:
            task_todo += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, task_done, task_todo + task_done))

    for todo in todos.json():
        if todo.get('completed') is True:
            print("\t {}".format(todo.get('title')))
