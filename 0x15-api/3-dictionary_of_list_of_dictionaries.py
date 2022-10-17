#!/usr/bin/python3
"""
Module for gathering user todos list from external API
"""
import json
import requests
import sys


def filter_item(username, todos):
    """ Filters usefull items from the todos dictionary """
    file_name = "todo_all_employees.json"
    todo_list = []

    for todo in todos:
        todo['task'] = todo.pop('title')
        del todo['userId']
        del todo['id']
        todo['username'] = username
        todo_list.append(todo)

    return todo_list


def export_to_json(todo_dict):
    """ Exports the fetched data to json file format. """
    file_name = "todo_all_employees.json"
    json_string = json.dumps(todo_dict)

    with open(file_name, 'w') as fs:
        fs.write(json_string)


def fetch_todos(base_url='https://jsonplaceholder.typicode.com/users'):
    """ Fetch the todos of the user with id = @id """

    users = requests.get(base_url)
    my_dict = {}
    for user in users.json():
        todo_url = base_url + "/{}/todos".format(user.get('id'))
        todos = requests.get(todo_url)
        username = user.get('username')
        id = user.get('id')
        todos = todos.json()
        lst = filter_item(username, todos)
        my_dict[id] = lst

    export_to_json(my_dict)


if __name__ == "__main__":
    fetch_todos()
