#!/usr/bin/python3
"""importing the libraries
"""

import requests
import sys
import csv

""""Gathering data from an API"""


def get_user(employee_id):
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(api_url)
    user = response.json()
    return user


def get_todo(employee_id):
    u = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(u)
    todos = response.json()
    return todos


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid integer for employee ID.")
        sys.exit(1)

    user = get_user(employee_id)
    name = user.get('name', f"User {employee_id}")
    todos = get_todo(employee_id)
    

    with open(f'{employee_id}.csv', 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": name,
                "TASK_COMPLETED_STATUS": todo['completed'],
                "TASK_TITLE": todo['title']
            })
if __name__ == "__main__":
    main()
