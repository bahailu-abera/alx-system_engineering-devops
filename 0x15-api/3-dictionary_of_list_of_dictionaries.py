#!/usr/bin/python3
"""
Module for gathering user todos list from external API
"""
import json
import requests
import sys


def export_to_json(username, id, todos):
    """ Exports the fetched data to json file format. """
    userid = id
    file_name = "todo_all_employees.json"

    todo_list = []

    for todo in todos:
        todo['task'] = todo.pop('title')
        del todo['userId']
        del todo['id']
        todo['username'] = username
        todo_list.append(todo)
    todo_dict = {}
    todo_dict[userid] = todo_list
    json_string = json.dumps(todo_dict)

    with open(file_name, 'a') as fs:
        fs.write(json_string)


def fetch_todos(base_url='https://jsonplaceholder.typicode.com/users'):
    """ Fetch the todos of the user with id = @id """

    users = requests.get(base_url)
    for user in users.json():
        todo_url = base_url + "/{}/todos".format(user.get('id'))
        todos = requests.get(todo_url)
        username = user.get('username')
        id = user.get('id')
        todos = todos.json()
        export_to_json(username, id, todos)


if __name__ == "__main__":
    fetch_todos()
