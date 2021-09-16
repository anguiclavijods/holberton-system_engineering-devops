#!/usr/bin/python3
""" Script that gather data from an API, For verify data of employees
    convert data to format csv"""
import csv
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

    with open(id_user + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in user_tasks:
            writer.writerow([user.get
                             ("id", None),
                             user.get("username"),
                             task.get("completed", None),
                             task.get("title", None)])
