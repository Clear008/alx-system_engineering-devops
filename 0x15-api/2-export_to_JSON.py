#!/usr/bin/python3
"""Export data in the JSON format of an employee."""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    user_id = sys.argv[1]
    username = user.get("username")

    with open("{}.json".format(user_id), "w") as file:
        json.dump({user_id: [{
                "task": s.get("title"),
                "completed": s.get("completed"),
                "username": username
            } for s in todos]}, file)
