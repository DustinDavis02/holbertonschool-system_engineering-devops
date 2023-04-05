#!/usr/bin/python3
"""
Gathers data from an API endpoint and exports it in JSON format
"""

import json
import requests


if __name__ == "__main__":
    # Define endpoint
    url = "https://jsonplaceholder.typicode.com/todos"

    # Send request to API and parse response
    response = requests.get(url)
    tasks = response.json()

    # Format data as JSON
    data = {}
    for task in tasks:
        user_id = task['userId']
        if user_id not in data:
            data[user_id] = []
        data[user_id].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": ""
        })

    # Get user names
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()
    for user in users:
        user_id = user['id']
        if user_id in data:
            for task in data[user_id]:
                task['username'] = user['username']

    # Write data to JSON file
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as file:
        json.dump(data, file)
