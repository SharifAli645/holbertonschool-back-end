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
    response = requests.get(url)
    json_data = response.json()
    emp_name = json_data.get('username')
    emp_id = json_data.get('id')

    url = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    response = requests.get(url)
    tasks = response.json()

    data = [[emp_id, emp_name, task.get("completed"), task.get("title")]
            for task in tasks]

    with open(f"{argv[1]}.csv", 'w') as fil3:
        writer = writer(fil3, quoting=QUOTE_ALL)
        writer.writerows(data)
