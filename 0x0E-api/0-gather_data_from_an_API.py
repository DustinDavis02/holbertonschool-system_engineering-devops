#!/usr/bin/python3
"""Gathers data from an API endpoint and prints the user's to-do list progress"""

import requests
import sys



if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) < 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)