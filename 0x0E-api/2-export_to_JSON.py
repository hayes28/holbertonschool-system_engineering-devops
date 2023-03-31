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
        print("Usage: {} EMPLOYEE_ID".format(argv[0]))
        exit(1)

    EMPLOYEE_ID = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        EMPLOYEE_ID)
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response.status_code))
        exit(1)

    todos = response.json()
    employee_name_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        EMPLOYEE_ID)
    response_name = requests.get(employee_name_url)

    if response_name.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response_name.status_code))
        exit(1)

    employee_name = response_name.json().get("username")
    filename = "{}.csv".format(EMPLOYEE_ID)

    user_tasks = []
    for todo in todos:
        completed_status = True if todo["completed"] else False
        user_tasks.append({
            'task': todo["title"],
            'completed': completed_status,
            'username': employee_name
        })

    data = {EMPLOYEE_ID: user_tasks}

    with open(filename, mode='w') as json_file:
        json.dump(data, json_file, indent=4)
