#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format
"""

import requests
from sys import argv
import json


if __name__ == '__main__':
    if len(argv) != 2:
        print(f"Usage: {argv[0]} EMPLOYEE_ID")
        exit(1)

    EMPLOYEE_ID = argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}/todos"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Request failed with status code {response.status_code}")
        exit(1)

    todos = response.json()
    employee_name_url = f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}"
    response_name = requests.get(employee_name_url)

    if response_name.status_code != 200:
        print(f"Error: Request failed with status code {response_name.status_code}")
        exit(1)

    employee_name = response_name.json().get("username")
    filename = f"{EMPLOYEE_ID}.json"

    user_tasks = []
    for todo in todos:
        completed_status = bool(todo["completed"])
        user_tasks.append({
            "task": todo["title"],
            "completed": completed_status,
            "username": employee_name
        })

    data = {EMPLOYEE_ID: user_tasks}

    with open(filename, mode='w') as json_file:
        json.dump(data, json_file, indent=4)
