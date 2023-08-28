#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    EMPLOYEE_NAME = ''
    NUMBER_OF_DONE_TASKS = ''
    TOTAL_NUMBER_OF_TASKS = ''

    url = f'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url).json()
    user_list = [{"username": user.get('username'), "id": user.get('id')}
                 for user in users]

    url = f'https://jsonplaceholder.typicode.com/todos/'
    todos = requests.get(url).json()

    dicty = {}
    for user in user_list:
        lista = []
        for todo in todos:
            if user.get('id') == todo.get('userId'):
                ele = {"username": user.get('username'),
                       "task": todo.get('title'),
                       "completed": todo.get('completed')}
                lista.append(ele)
        dicty.update({str(user.get('id')): lista})
    with open("todo_all_employees.json", 'w') as fil3:
        fil3.write(json.dumps(dicty))
