#!/usr/bin/python3
"""This module defines a script that using an REST API, for a given employee ID
and returns information about his/her"""


if __name__ == "__main__":
    import json
    import requests

    url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users".format(url)
    filename = "todo_all_employees.json"
    dictionary = {}

    req_user = requests.get(user_url).json()
    for user in req_user:
        user_id = user.get('id')
        user_name = user.get('username')

        todo_url = "{}/{}/todos".format(user_url, user_id)
        req_todo = requests.get(todo_url).json()
        list_task = []
        for task in req_todo:
            dict_task = {"username": user_name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            list_task.append(dict_task)
        dictionary[user_id] = list_task
    to_json = json.dumps(dictionary)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(to_json)

