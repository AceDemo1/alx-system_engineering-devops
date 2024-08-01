#!/usr/bin/python3
"""This module defines a script that using an REST API, for a given employee ID
and returns information about his/her TODO list progress"""


if __name__ == "__main__":
    import requests
    from sys import argv

    # formatting url
    url = "https://jsonplaceholder.typicode.com"
    user_id = int(argv[1])
    user_url = "{url}/users/{id}".format(url=url, id=user_id)
    todos_url = "{user_url}/todos".format(user_url=user_url)

    # get request
    req_user = requests.get(user_url).json()
    req_todos = requests.get(todos_url).json()

    # get information thanks the request
    user_name = req_user.get('name')
    total_tasks = len(req_todos)
    completed_task = []
    for value in req_todos:
        if value.get('completed') is True:
            completed_task.append(value.get('title'))
    non_completed_task = total_tasks - len(completed_task)

    # print information
    print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                          len(completed_task),
                                                          total_tasks))
    for title in completed_task:
        print("\t {}".format(title))


