#!/usr/bin/python3
"""Script that gather data from an API"""
import requests
import sys

id_user = (sys.argv[1])
response_users = requests.get("https://jsonplaceholder.typicode.com/users/" + str(id_user))
user = response_users.json()
print("Employee {} is done with".format(user["name"]))

response_todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId=" + str(id_user))
user_tasks = response_todo.json()
total_tasks = len(user_tasks)

url = "https://jsonplaceholder.typicode.com/todos?userId={}&completed=true".format(id_user)
response_todo_completed = requests.get(url)
todo_completed = response_todo_completed.json()
total_completed = len(todo_completed)
print(str(total_completed) + "/" + str(total_tasks))

for user_task in user_tasks:
    print(user_task["title"])

print("Employee {} is done with tasks {}".format(user["name"], len(user_tasks ))