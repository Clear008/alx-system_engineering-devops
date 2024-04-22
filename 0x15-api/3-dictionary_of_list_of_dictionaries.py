#!/usr/bin/python3
"""Export data in the JSON format of all employees."""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as file:
        json.dump({
            r.get("id"): [{
                "task": s.get("title"),
                "completed": s.get("completed"),
                "username": r.get("username")
            } for s in requests.get(url + "todos",
                                    params={"userId": r.get("id")}).json()]
            for r in users}, file)
