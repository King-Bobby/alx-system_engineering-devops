#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""

import csv
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
        print(f"\t{task['title']}")

    # Export data to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = [
                'USER_ID', 'USERNAME',
                'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for task in todo_list:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_data['username'],
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })


if __name__ == "__main__":
    # Check if the employee ID argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_employee_todo_list(employee_id)
    except ValueError:
        print("Invalid employee ID. Please provide a valid integer.")
        sys.exit(1)
