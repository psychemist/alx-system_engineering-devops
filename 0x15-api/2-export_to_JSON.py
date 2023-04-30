#!/usr/bin/python3
"""Queries a REST API using a request for a given employee ID
and returns information about their TODO list progress
and saves the results to a json file
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(argv[1]))
    todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos/"
                         .format(argv[1]))

    u_name = user.json().get('username')
    u_id = str(user.json().get('id'))
    tasks = {u_id: []}

    for todo in todos.json():
        task = {"task": todo.get('title'), "completed": todo.get('completed'),
                "username": u_name}
        tasks[u_id].append(task)

    with open(str(u_id) + '.json', 'w') as f:
        f.write(json.dumps(tasks))
