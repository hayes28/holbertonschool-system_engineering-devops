#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format
"""
import requests
import json


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response.status_code))
        exit(1)

    todos = response.json()
    users_url = "https://jsonplaceholder.typicode.com/users"
    response_users = requests.get(users_url)

    if response_users.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response_users.status_code))
        exit(1)

    users = response_users.json()
    todo_all_employees = {}

    for user in users:
        user_id = user['id']
        employee_name = user['username']
        employee_todos = []

        for todo in todos:
            if todo['userId'] == user_id:
                employee_todos.append({
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": employee_name
                })

        todo_all_employees[user_id] = employee_todos

    with open("todo_all_employees.json", mode='w') as outfile:
        json.dump(todo_all_employees, outfile)
