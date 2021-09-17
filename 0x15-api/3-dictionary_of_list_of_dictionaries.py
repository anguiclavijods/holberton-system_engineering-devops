#!/usr/bin/python3
""" Script that gather data from an API, For verify data of employees
    convert data to format json"""
import json
import requests


if __name__ == "__main__":

    response_users = requests \
        .get("https://jsonplaceholder.typicode.com/users/")
    user = response_users.json()

with open('todo_all_employees.json', 'w', newline='') as file:
    json.dump(user, file)
