#!/usr/bin/python3
"""
Module returns information
about TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    """ Collects emplyee ID. """

    response = requests.get(f"https://jsonplaceholder"
                            f".typicode.com/todos?userId={employee_id}")
    todos = response.json()
    """
    Retrieve employee TODO list via
    request to API and parse response.
    """

    total_completed_tasks = 0
    total_tasks = len(todos)
    completed_tasks_titles = []

    for todo in todos:
        if todo["completed"]:
            total_completed_tasks += 1
            completed_tasks_titles.append(todo["title"])

    response = requests.get(f"https://jsonplaceholder"
                            f".typicode.com/users/{employee_id}")

    employee_name = response.json()["name"]
    """ Retrieve employee name. """

    print(f"Employee {employee_name} is done"
          f" with tasks({total_completed_tasks}/{total_tasks}):")

    for title in completed_tasks_titles:
        print(f"\t {title}")
