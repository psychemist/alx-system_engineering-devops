#!/usr/bin/python3
"""Queries a REST API using a request for all employees
and returns information about their TODO list progress
then saves the results to a json file
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users/")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/")

    task_dict = {}

    for user in users.json():
        u_name = user.get('username')
        u_id = str(user.get('id'))

        tasks = []
        for todo in todos.json():

            if int(u_id) == todo.get('userId'):
                task = {"username": u_name, "task": todo.get('title'),
                        "completed": todo.get('completed')}
                tasks.append(task)
        task_dict[u_id] = tasks

    with open('todo_all_employees.json', 'w') as f:
        f.write(json.dumps(task_dict))
