#!/usr/bin/python3
"""
Export to CSV
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
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

            csv_filename = f"{employee_id}.csv"

            with open(csv_filename, mode="w", newline="") as csv_file:
                csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

                for task in tasks:
                    csv_writer.writerow([employee_id, employee_name, task["completed"], task["title"]])
