#!/usr/bin/python3
"""
Module exports TODO list
progress to csv file.
"""
import csv
import requests
import sys

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

filename = (f"{employee_id}.csv")
""" Retrieve employee name and define csv file. """

with open(filename, 'w', newline="") as csv_file:
    """ Writes employee TOD list progress to a csv file. """
    writer = csv.writer(csv_file)
    writer.writerow(["USER_ID", "USERNAME",
                     "TASK_COMPLETED_STATUS", "TASK_TITLE"])
    for todo in todos:
        if not todo["completed"]:
            writer.writerow([employee_id, employee_name,
                            "False", todo["title"]])

    for todo in todos:
        if todo["completed"]:
            writer.writerow([employee_id, employee_name,
                            "True", todo["title"]])
