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
    if response.status_code == 200:
        json_data = response.json()
        emp_name = json_data.get('username')
        emp_id = json_data.get('id')

    url = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    response = requests.get(url)
    if response.status_code == 200:
        tasks = response.json()

    for task in tasks:
        with open(f"{argv[1]}.csv", 'a') as fil3:
            fil3.write(f'"{emp_id}", "{emp_name}", "{task.get("completed")}", \
"{task.get("title")}"' + "\n")
