#!/usr/bin/python3
"""Queries a REST API using a request for a given employee ID
and returns information about their TODO list progress
and saves the results to a csv file
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(argv[1]))
    todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos/"
                         .format(argv[1]))

    u_name = (user.json().get('username'))
    u_id = (user.json().get('id'))
    tasks = []

    for todo in todos.json():
        task = (u_id, u_name, todo.get('completed'), todo.get('title'))
        tasks.append(task)

    with open(str(u_id + 1) + '.csv', 'w') as f:
        for task in tasks:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(task)
