#!/usr/bin/python3

import requests
import sys

""" Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""


def get_employee_todo_progress(e_id):
    try:
        # get the employee info
        employee_url = f'https://jsonplaceholder.typicode.com/todos/{e_id}'
        response_employee = requests.get(employee_url)
        employee_data = response_employee.json()

        # print(employee_data)

        e_name = employee_data['title']

        # get the employee's todos
        todos_url = f'https://jsonplaceholder.typicode.com/users/{e_id}/todos'
        response_todos = requests.get(todos_url)
        todos_data = response_todos.json()

        # calculate the progress
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task['completed']]
        nodt = len(done_tasks)

        # Print the progress
        print(f'Employee {e_name} is done with tasks({nodt}/{total_tasks}):')

        for task in done_tasks:
            print(f'\t {task["title"]}')

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <e_id>")
    else:
        try:
            e_id = int(sys.argv[1])
            get_employee_todo_progress(e_id)
        except ValueError:
            print("The employee ID must be an integer.")
