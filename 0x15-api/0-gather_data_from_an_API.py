#!/usr/bin/python3
"""
Module returns TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    """ Collect employee ID from Command Line. """

    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    employee_name = response.json()['name']
    """
    Retrieve complete information about employee with target ID
    in JSON format then isolate name.
    """

    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    employee_todo_list = response.json()
    """
    Retrieve employee's todo list with the
    given ID.
    """

    total_tasks = len(employee_todo_list)
    total_completed_tasks = 0
    completed_tasks = []

    for tasks in employee_todo_list:
        """
        Count completed tasks and
        compile them into new list.
        """
        if tasks['completed']:
            completed_tasks.append(tasks['title'])
            total_completed_tasks += 1

    print(f'Employee {employee_name} is done with tasks('
          f'{total_completed_tasks}/{total_tasks}):')
    for item in completed_tasks:
        print(f'\t{item}')
