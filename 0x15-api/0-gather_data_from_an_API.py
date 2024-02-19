#!/usr/bin/python3
"""importing the libraries"""
import requests
import sys


def get_user(employee_id):
    """get user details"""
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(api_url)
    user = response.json()
    return user


def get_todo(employee_id):
    """get the info about todo list progress"""
    u = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(u)
    todos = response.json()
    return todos


def main():
    """calculating the progress"""
    """Check if an argument is provided"""
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    """Get the employee ID from the command line argument"""
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid integer for employee ID.")
        sys.exit(1)

    """Call the function to get user details"""
    user = get_user(employee_id)
    user_name = user.get('name', f"User {employee_id}")

    """Call the function to get the TODO list"""
    todos = get_todo(employee_id)

    total_tasks = len(todos)
    task_completed = sum(1 for todo in todos if todo['completed'])

    """output"""
    print(f"Employee {user_name} is done with tasks(
        {task_completed}/{total_tasks}): ")
    for todo in todos:
        if todo['completed']:
            print(f"     {todo['title']}")


if __name__ == "__main__":
    main()
