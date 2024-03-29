#!/usr/bin/python3
"""Gathers data from an API endpoint and prints the user's to-do list progress"""

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

    # Count number of completed tasks
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    
    # Get user's name
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)
    employee_name = response.json()['name']

   # Print progress report
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                           completed_tasks,
                                                           total_tasks))
    for task in tasks:
        if task['completed']:
            print("\t {}".format(task['title']))