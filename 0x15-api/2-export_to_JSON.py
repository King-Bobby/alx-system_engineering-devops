#!/usr/bin/python3
"""
MOdule 2-export_to_JSON
"""


import json
import requests
import sys


def fetch_employee_todo_list(employee_id):
    """
    Fetches data from the API for a given employee ID, displays the
    TODO list progress,and exports the data in JSON format.

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
    completed_tasks = [{
        'task': task['title'],
        'completed': task['completed'],
        'username': employee_data['username']
    } for task in todo_list]

    # Display the result
    tasks = len(todo_list)
    comp_tasks = len(completed_tasks)
    emp_name = employee_data['name']
    print(f"Employee {emp_name} is done with tasks({comp_tasks}/{tasks}):")
    for task in completed_tasks:
        print(f"\t{task['task']}")

    # Export data to JSON
    json_data = {str(employee_id): completed_tasks}
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    # Check if the employee ID argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_employee_todo_list(employee_id)
    except ValueError:
        print("Invalid employee ID. Please provide a valid integer.")
        sys.exit(1)
