#!/usr/bin/python3
"""
Gathers data from an API endpoint and exports it in JSON format
"""

import json
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

    # Format data as JSON
    data = {employee_id: []}
    for task in tasks:
        data[employee_id].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        })

    # Write data to JSON file
    filename = "{}.json".format(employee_id)
    with open(filename, mode='w') as file:
        json.dump(data, file)
