#!/usr/bin/python3
"""
Module that gathers data from an API
"""


import requests
import sys


def fetch_employee_todo_list(employee_id):
    """
    Fetches data from the API for a given employee ID
    and displays the TODO list progress.
    Args:
        employee_id (int): The ID of the employee.
    Returns:
        None
    """
    # Make a request to the API to get the employee data
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    employee_data = response.json()

    # Make another request to get the employee's TODO list
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    todo_list = response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todo_list if task['completed']]

    # Display the result
    tasks = len(todo_list)
    comp_tasks = len(completed_tasks)
    emp_name = employee_data['name']
    print(f"Employee {emp_name} is done with tasks({comp_tasks}/{tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    # Check if the employee ID argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_employee_todo_list(employee_id)
    except ValueError:
        print("Invalid employee ID. Please provide a valid integer.")
        sys.exit(1)
