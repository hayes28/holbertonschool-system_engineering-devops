#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export
data in the CSV format.
"""

import requests
from sys import argv
import csv


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
    filename = f"{EMPLOYEE_ID}.csv"

    with open(filename, mode='w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for todo in todos:
            completed_status = "True" if todo["completed"] else "False"
            writer.writerow({
                'USER_ID': EMPLOYEE_ID,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': completed_status,
                'TASK_TITLE': todo["title"]
            })
