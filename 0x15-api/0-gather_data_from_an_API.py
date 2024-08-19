#!/usr/bin/python3

import requests
import sys

"""
Python script that, using this REST API
(https://jsonplaceholder.typicode.com),
for a given employee ID, returns information
about his/her TODO list progress.

The script accepts an integer as a parameter,
which is the employee ID.
It displays on the standard output the employee
TODO list progress in this exact format:

First line: Employee EMPLOYEE_NAME is done with
tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    EMPLOYEE_NAME: name of the employee
    NUMBER_OF_DONE_TASKS: number of completed tasks
    TOTAL_NUMBER_OF_TASKS: total number of tasks,
    which is the sum of
    completed and non-completed tasks
Second and subsequent lines display the title of
completed tasks:
TASK_TITLE (with 1 tabulation and 1 space
before the TASK_TITLE)

Example:
    python3 0-gather_data_from_an_API.py 2
    Employee Ervin Howell is done with tasks(8/20):
         distinctio vitae autem nihil ut molestias quo
         voluptas quo tenetur perspiciatis explicabo natus
         aliquam aut quasi
         veritatis pariatur delectus
         nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
         repellendus veritatis molestias dicta incidunt
         excepturi deleniti adipisci voluptatem et neque optio illum ad
         totam atque quo nesciunt
"""


def get_employee_todo_progress(e_id):
    """
    Function to fetch and display employee TODO list progress.

    Parameters:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
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
