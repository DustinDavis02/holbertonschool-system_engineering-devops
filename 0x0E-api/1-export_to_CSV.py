#!/usr/bin/python3
"""Gathers data from an API endpoint and exports it in CSV format"""

import csv
import requests
import sys


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) < 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    # Define endpoint and employee ID
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(sys.argv[1])
    employee_id = sys.argv[1]

    # Send request to API and parse response
    response = requests.get(url)
    tasks = response.json()

    # Get user's name
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)
    employee_name = response.json()['username']

    # Write data to CSV file
    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for task in tasks:
            writer.writerow([employee_id, employee_name, task['completed'], task['title']])
