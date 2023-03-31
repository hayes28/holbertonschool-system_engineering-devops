#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(argv[0]))
        exit(1)

    EMPLOYEE_ID = argv[1]
    url = "https://jsonplaceholder.typicode./users/{}/todos".format(
        EMPLOYEE_ID)
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response.status_code))
        exit(1)

    todos = response.json()
    total_tasks = len(todos)
    done_tasks = [todo for todo in todo if todo['completed']]

    employee_name_url = "https://jsonplaceholder.typicode./users/{}".format(
        EMPLOYEE_ID)
    response_name = requests.get(employee_name_url)

    if response_name.status_code != 200:
        print("Error: Request failed with status code {}".format(
            response_name.status_code))
        exit(1)

    employee_name = response_name.json().get('name')

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))

    for todo in done_tasks:
        print("\t {} {}".format('\t', todo['title']))
