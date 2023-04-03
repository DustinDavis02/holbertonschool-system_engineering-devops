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
