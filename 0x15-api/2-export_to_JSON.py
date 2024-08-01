#!/usr/bin/python3
"""This module defines a script that using an REST API, for a given employee ID
and returns information about his/her TODO list progress"""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com"
    user_id = argv[1]
    user_url = "{}/users/{}".format(url, user_id)
    todos_url = "{}/todos".format(user_url)

    req_user = requests.get(user_url).json()
    req_todos = requests.get(todos_url).json()

    user_name = req_user.get('username')

    filename = "{}.json".format(user_id)

    list_element = []
    for value in req_todos:
        dictionary = {"task": value.get('title'),
                      "completed": value.get('completed'),
                      "username": user_name}
        list_element.append(dictionary)
    json_dictionary = {user_id: list_element}
    to_json = json.dumps(json_dictionary)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(to_json)


