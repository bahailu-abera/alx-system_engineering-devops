#!/usr/bin/python3
"""
Module for gathering user todos list from external API
"""
import requests
import sys


def print_completed(name, todos):
    """ Prints out completed list of todos """
    comp_title = ""
    comp_total = 0

    for todo in todos:
        if todo.get('completed'):
            comp_title = comp_title + "\n\t" + todo.get('title')
            comp_total += 1
    print("Employee {} is done with tasks({:d}/{:d}):".
           format(name, comp_total, len(todos)), end="")
    print("{}".format(comp_title))


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
        print_completed(name, todos_dict)


if __name__ == "__main__":
    argv = sys.argv
    fetch_todos(argv[1])
