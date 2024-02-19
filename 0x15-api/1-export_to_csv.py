#!/usr/bin/python3
"""export data in the csv format"""


import requests
import csv
from sys import argv

if __name__ == "__main__":
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1])).json()
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json()

    with open('{}.csv'.format(argv[1]), mode='w', newline="") as file:
        csv_writer = csv.writer(file, quoting = csv.QUOTE_ALL)
        
        for t in todo:
            csv_writer.writerow([argv[1], users['name'], t['completed'], t['title']])
