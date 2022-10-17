#!/usr/bin/python3
"""
Module for gathering user todos list from external API
"""
import json
import requests
import sys


def export_to_json(username, todos):
    """ Exports the fetched data to json file format. """
    userid = todos[0].get('userId')
    file_name = "{}.json".format(userid)

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

    with open(file_name, 'w') as fs:
        fs.write(json_string)


def fetch_todos(id, url='https://jsonplaceholder.typicode.com/users'):
    """ Fetch the todos of the user with id = @id """
    user_url = url + "/" + id
    todos_url = user_url + "/todos"

    user = requests.get(user_url)
    todos = requests.get(todos_url)
    username = ""
    todos_dict = None

    if user.status_code == 200:
        username = user.json().get('username')
    if todos.status_code == 200:
        todos_dict = todos.json()
    if username and todos_dict:
        export_to_json(username, todos_dict)


if __name__ == "__main__":
    argv = sys.argv
    fetch_todos(argv[1])
