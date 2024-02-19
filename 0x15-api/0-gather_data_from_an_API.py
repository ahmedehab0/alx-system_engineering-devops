#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos?userId={}".format(sys.argv[1])).json()

    completed = [t["title"] for t in todos if t["completed"] is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(completed), len(todos)))
    for c in completed:
        print("\t {}".format(c))
