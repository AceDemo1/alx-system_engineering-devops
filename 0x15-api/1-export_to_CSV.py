#!/usr/bin/python3
"""This module defines a script that using an REST API, for a given employee ID
and returns information about his/her"""


if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com"
    user_id = argv[1]
    user_url = "{}/users/{}".format(url, user_id)
    todos_url = "{}/todos".format(user_url)

    req_user = requests.get(user_url).json()
    req_todos = requests.get(todos_url).json()

    user_name = req_user.get('username')

    filename = "{}.csv".format(user_id)
    with open(filename, 'w', encoding='utf-8') as f:
        csv_writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)

        for value in req_todos:
            data = [user_id, user_name, value.get('completed'),
                    value.get('title')]
            csv_writer.writerow(data)


