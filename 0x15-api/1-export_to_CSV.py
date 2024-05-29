#!/usr/bin/python3
"""
Module lists todo list items of employee.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    employee_info = response.json()
    """
    Retrieve complete information about  employee
    with target ID in JSON format.
    """

    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    employee_todo_list = response.json()
    """
    Retrieve employee's todo list with the
    given ID.
    """

row_data = []
for item in employee_todo_list:
    """
    Format each row to contain ID, username, task completion status
    and all task titles, in this order then append to new list.
    """
    row = [
        item['userId'],
        employee_info['username'],
        item['completed'],
        item['title']
        ]
    row_data.append(row)

with open('USER_ID.csv', 'w', newline='') as csvFile:
    """
    Write into new CSV file the tasks belonging to an employee
    according to defined format.
    """
    writer = csv.writer(csvFile)
    for row in row_data:
        writer.writerow(row)
