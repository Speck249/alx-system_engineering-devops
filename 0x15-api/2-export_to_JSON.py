#!/usr/bin/python3
"""
Module exports to-do list
progress to json file.
"""
import json
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

    response = requests.get(f"https://jsonplaceholder"
                            f".typicode.com/users/{employee_id}")
    employee_name = response.json()["username"]

    filename = (f"{employee_id}.json")
    todo_progress = {employee_id: []}
    """ Dictionary stores to-do list progress. """

    for todo in todos:
        task = {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": employee_name
        }
        todo_progress[employee_id].append(task)

    with open(filename, "w") as json_file:
        json.dump(todo_progress, json_file)
