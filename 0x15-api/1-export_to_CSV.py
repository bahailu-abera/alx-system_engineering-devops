#!/usr/bin/python3
"""
Module for gathering user todos list from external API
"""
import csv
import requests
import sys


def export_to_csv(username, todos):
    """ Exports the fetched data to csv file format. """
    file_name = "{}.csv".format(todos[0].get('userId'))
    header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(file_name, 'w') as fs:
        writer = csv.DictWriter(fs, fieldnames=header, quoting=csv.QUOTE_ALL)
        for todo in todos:
            row = {}
            row['USER_ID'] = todo.get('userId')
            row['USERNAME'] = username
            row['TASK_COMPLETED_STATUS'] = todo.get('completed')
            row['TASK_TITLE'] = todo.get('title')
            writer.writerow(row)


def fetch_todos(id, url='https://jsonplaceholder.typicode.com/users'):
    """ Fetch the todos of the user with id = @id """
    user_url = url + "/" + id
    todos_url = user_url + "/todos"

    user = requests.get(user_url)
    todos = requests.get(todos_url)
    name = ""
    todos_dict = None

    if user.status_code == 200:
        name = user.json().get('name')
    if todos.status_code == 200:
        todos_dict = todos.json()
    if name and todos_dict:
        export_to_csv(name, todos_dict)


if __name__ == "__main__":
    argv = sys.argv
    fetch_todos(argv[1])
