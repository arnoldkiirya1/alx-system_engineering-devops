#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
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

            total_tasks = len(tasks)
            done_tasks = [task for task in tasks if task["completed"]]
            total_done_tasks = len(done_tasks)

            print(f"Employee {employee_name} is done with tasks({total_done_tasks}/{total_tasks}):")

            for task in done_tasks:
                print(f"\t {task['title']}")
