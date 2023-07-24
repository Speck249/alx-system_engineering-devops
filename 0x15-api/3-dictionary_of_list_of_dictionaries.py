#!/usr/bin/python3
"""
Module exports to-do list
progress to json file.
"""
import json
import requests

response = requests.get(f"https://jsonplaceholder"
                        f".typicode.com/todos")
todos = response.json()
"""
Retrieve employee TODO list via
request to API and parse response.
"""

employee_todo_list = {}

for todo in todos:
    employee_id = todo["userId"]
    if employee_id not in employee_todo_list:
        employee_todo_list[employee_id] = []

        response = requests.get(f"https://jsonplaceholder"
                                f".typicode.com/users/{employee_id}")
        employee_name = response.json()["name"]

    task = {
            "username": employee_name,
            "task": todo["title"],
            "completed": todo["completed"]
    }
    employee_todo_list[employee_id].append(task)

filename = "todo_all_employees.json"
with open(filename, "w") as json_file:
    json.dump(employee_todo_list, json_file)
