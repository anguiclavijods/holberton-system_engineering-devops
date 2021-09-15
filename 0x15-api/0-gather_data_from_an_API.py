#!/usr/bin/python3
""" Script that gather data from an API,
    For verify data of employes """
import requests
import sys

if __name__ == "__main__":

    id_user = (sys.argv[1])
    response_users = requests\
        .get("https://jsonplaceholder.typicode.com/users/" + str(id_user))
    user = response_users.json()

    response_todo = requests.get("https://jsonplaceholder"
                                 ".typicode.com/todos?userId=" + str(id_user))
    user_tasks = response_todo.json()
    total_tasks = len(user_tasks)

    url = "https://jsonplaceholder." \
          "typicode.com/todos?userId={}&completed=true".format(id_user)
    response_todo_completed = requests.get(url)
    todo_completed = response_todo_completed.json()
    total_completed = len(todo_completed)

    print("Employee {} is done with tasks({}):".format(
        user.get("name", None), str(total_completed) + "/" + str(total_tasks)))
    for user_task in todo_completed:
        print("\t {}".format(user_task.get("title", None)))
