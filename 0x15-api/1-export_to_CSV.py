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
        tasks.append((todo.get('completed'), todo.get('title')))

    with open(str(u_id) + '.csv', 'w') as f:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]

        for task in tasks:
            writer = csv.DictWriter(f, fieldnames=fieldnames,
                                    quoting=csv.QUOTE_ALL)
            writer.writerow({"USER_ID": u_id, "USERNAME": u_name,
                         "TASK_COMPLETED_STATUS": task[0],
                         "TASK_TITLE": task[1]})
