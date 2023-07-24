#!/usr/bin/python3
"""
Python script that fetches tasks for all employees using the given
REST API (https://jsonplaceholder.typicode.com/),
and exports the data in JSON format.
"""


import json
import requests


def get_all_employee_tasks():
    base_url = 'https://jsonplaceholder.typicode.com/'
    users_url = base_url + 'users'
    todos_url = base_url + 'todos'

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200:
        print("Error fetching user data")
        return None

    if todos_response.status_code != 200:
        print("Error fetching tasks")
        return None

    users_data = users_response.json()
    tasks_data = todos_response.json()

    all_employee_tasks = {}
    for user in users_data:
        employee_id = user['id']
        employee_username = user['username']
        employee_tasks = []
        for task in tasks_data:
            if task['userId'] == employee_id:
                task_data = {
                    'username': employee_username,
                    'task': task['title'],
                    'completed': task['completed']
                }
                employee_tasks.append(task_data)
        all_employee_tasks[str(employee_id)] = employee_tasks
    return all_employee_tasks


def export_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    tasks = get_all_employee_tasks()

    if tasks is not None:
        filename = 'todo_all_employees.json'
        export_to_json(tasks, filename)
