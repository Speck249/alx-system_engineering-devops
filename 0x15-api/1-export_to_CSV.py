#!/usr/bin/python3
"""
Module exports TODO list
progress to csv file.
"""
import csv
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

    filename = (f"{employee_id}.csv")
    """ Retrieve employee name and define csv file. """

    with open(filename, 'w', newline="") as csv_file:
        """ Writes employee TOD list progress to a csv file. """
        for todo in todos:
            csv_file.write('"{}","{}","{}","{}"\n'.format(employee_id,
                                                          employee_name,
                                                          todo["completed"],
                                                          todo["title"]))
