#!/usr/bin/python3
"""Export data in the CSV format of an employee."""
import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    user_id = sys.argv[1]

    with open("{}.csv".format(user_id), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        writer.writerow(["User ID", "Username", "Completed", "Title"])

        for todo in todos:
            writer.writerow([user_id, user.get("username"),
                             todo.get("completed"), todo.get("title")])
