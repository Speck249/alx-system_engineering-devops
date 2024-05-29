#!/usr/bin/python3
"""
Module saves API response to JSON file.
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    employee_info = response.json()
    """
    Retrieve complete information about employee with
    target ID in JSON format.
    """

    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response = requests.get(url)
    employee_todo_list = response.json()
    """
    Retrieve employee's todo list with the
    given ID.
    """

row_data = {employee_id: []}
for item in employee_todo_list:
    """
    Format each row with target information about
    employee's todo list along with name.
    """
    row = {
        'task': item['title'],
        'completed': item['completed'],
        'username': employee_info['username']
    }
    row_data[employee_id].append(row)

with open('USER_ID.json', 'w') as File:
    """
    Save into JSON file serialized employee data.
    """
    json.dump(row_data, File)
