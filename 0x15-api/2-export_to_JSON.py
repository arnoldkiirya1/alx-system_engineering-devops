#!/usr/bin/python3
"""
Export to JSON
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./2-export_to_JSON.py <employee_id>")
    else:
        employee_id = int(argv[1])
        user_info = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        ).json()

        if "name" in user_info:
            employee_name = user_info["name"]

            tasks = requests.get(
                f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
            ).json()

            json_filename = f"{employee_id}.json"
            task_list = []

            for task in tasks:
                task_info = {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": employee_name
                }
                task_list.append(task_info)

            user_data = {str(employee_id): task_list}

            with open(json_filename, mode="w") as json_file:
                json.dump(user_data, json_file)
