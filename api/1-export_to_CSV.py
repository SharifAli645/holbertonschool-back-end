#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv
from csv import writer, QUOTE_ALL


if __name__ == "__main__":

    url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    user = requests.get(url).json()
    emp_name = user.get('username')
    emp_id = user.get('id')

    url = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    todo = requests.get(url).json()

    data = [[emp_id, emp_name, task.get("completed"), task.get("title")]
            for task in todo]

    with open(f"{argv[1]}.csv", 'w') as fil3:
        writer = writer(fil3, quoting=QUOTE_ALL)
        writer.writerows(data)
