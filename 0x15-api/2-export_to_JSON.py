#!/usr/bin/python3
""" Script that gather data from an API, For verify data of employees
    convert data to format json"""
import csv
import json
import requests
import sys

if __name__ == "__main__":

    id_user = (sys.argv[1])
    response_users = requests \
        .get("https://jsonplaceholder.typicode.com/users/" + str(id_user))
    user = response_users.json()

    response_todo = requests.get("https://jsonplaceholder"
                                 ".typicode.com/todos?userId=" + str(id_user))
    user_tasks = response_todo.json()

    format_tasks = []
    for task in user_tasks:
        task_dict = {}
        task_dict.update({"task": task.get("title", None)})
        task_dict.update({"completed": task.get("completed", None)})
        task_dict.update({"username": user.get("username", None)})
        format_tasks.append(task_dict)
    data = {user.get("id"): format_tasks}

    with open(id_user + '.json', 'w', newline='') as file:
        json.dump(data, file)
