#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":

    url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    response = requests.get(url)
    json_data = response.json()
    emp_name = json_data.get('name')

    url = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    response = requests.get(url)
    json_data = response.json()
    tasks = len(json_data)
    done_tasks = [x for x in json_data if x.get('completed')]
    num_task = len(done_tasks)

    print(f'Employee {emp_name} is done with tasks ({num_task}/{tasks}):')
    for x in done_tasks:
        print(f"\t {x.get('title')}")
