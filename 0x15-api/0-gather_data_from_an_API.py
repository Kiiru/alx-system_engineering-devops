import requests
import sys

def get_employee_todo_progress(employee_id):
    try:
        # get the employee info
        employee_url = f'https://jsonplaceholder.typicode.com/todos/{employee_id}'
        response_employee = requests.get(employee_url)
        employee_data = response_employee.json()

        # print(employee_data)

        employee_name = employee_data['title']

        # get the employee's todos
        todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
        response_todos = requests.get(todos_url)
        todos_data = response_todos.json()

        # calculate the progress
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task['completed']]
        number_of_done_tasks = len(done_tasks)

        # Print the progress
        print(f'Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):')

        for task in done_tasks:
            print(f'\t {task["title"]}')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("The employee ID must be an integer.")
