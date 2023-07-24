#!/usr/bin/python3
"""
Module exports to-do list
progress to json file.
"""
import json
import requests

if __name__ == "__main__":
    response = requests.get(f"https://jsonplaceholder"
                            f".typicode.com/users")

    employees = response.json()
    """
    Retrieve employee TODO list via
    request to API and parse response.
    """

    employee_todo_list = {}

    for employee in employees:
        employee_id = employee.get("id")
        employee_name = employee.get("username")

        response = requests.get(f"https://jsonplaceholder"
                                f".typicode.com/users/{employee_id}/todos/")
        todos = response.json()

        employee_todo_list[employee_id] = []

        for todo in todos:
            employee_todo_list[employee_id].append({
                "username": employee_name,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            })

    filename = "todo_all_employees.json"
    with open(filename, "w") as json_file:
        json.dump(employee_todo_list, json_file)
