#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import json
from sys import argv


if __name__ == "__main__":

    url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        emp_user = json_data.get('username')
        emp_id = json_data.get('id')

    url = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        tasks = [x for x in json_data]

    lista = []
    for task in tasks:
        lista.append({"task": task.get('title'),
                      "completed": task.get('completed'),
                      "username": emp_user})

    with open(f"{emp_id}.json", 'w') as fil3:
        fil3.write(json.dumps({emp_id: lista}))
