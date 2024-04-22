#!/usr/bin/python3
"""Export data in the CSV format of an employee."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, s.get("completed"), s.get("title")]
         ) for s in todos]
