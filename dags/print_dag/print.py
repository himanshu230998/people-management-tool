# read.py
import os

dag_id_prefix_placeholder = ""
task_id_prefix_placeholder = ""
name_prefix_placeholder = ""
dag_id = f"{dag_prefix_placeholder}google_adwords"

# Access the environment variable
github_push_name = os.getenv("GITHUB_PUSH_NAME")

if github_push_name:
    print(github_push_name, dag_id)
else:
    print("No push name provided. m4")


























































