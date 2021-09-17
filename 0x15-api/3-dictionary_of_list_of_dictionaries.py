#!/usr/bin/python3
""" Script that gather data from an API, For verify data of employees
    convert data to format json"""
import json
import requests


if __name__ == "__main__":

    response_users = requests \
        .get("https://jsonplaceholder.typicode.com/users/")
    users = response_users.json()

    response_todos = requests.\
        get("https://jsonplaceholder.typicode.com/todos")
    todos = response_todos.json()

    format_task = {}
    list_task = []
    format_task_dict = {}
    for user in users:
        for todo in todos:
            if todo.get("userId") == user.get("id"):
                format_task.update({"username": user.get("username", None)})
                format_task.update({"task": todo.get("title", None)})
                format_task.update({"completed": todo.get("completed", None)})
                list_task.append(dict(format_task))
        format_task_dict[user.get("id")] = list(list_task)
        list_task.clear()

    with open('todo_all_employees.json', 'w', newline='') as file:
        json.dump(format_task_dict, file)
