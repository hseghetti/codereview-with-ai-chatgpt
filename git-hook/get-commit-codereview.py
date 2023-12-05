#!/usr/bin/env python3
import datetime
import json
import requests
from subprocess import check_output

log = check_output(["git", "log", "-1", "--stat", "HEAD"])
diff = check_output(["git", "diff", "HEAD^", "HEAD"])
files_changed = check_output(["git", "diff", "--name-only", "HEAD^", "HEAD"])
commit_message = log.decode("utf-8").split("\n")[4]
commit_code_changes = diff.decode("utf-8").split("\n")[4:-1]
files_changed = files_changed.decode("utf-8").split("\n")[:-1]
commit_hash = log.decode("utf-8").split("\n")[0].split(" ")[1]

def codereview(commit_message, commit_code_changes, files_changed, commit_hash):
    url = "http://localhost:8000/post"
    data = {
        "commit_message": json.dumps(commit_message),
        "commit_description": "",
        "commit_code_changes": json.dumps(commit_code_changes),
        "files_changed": json.dumps(files_changed),
        "commit_hash": json.dumps(commit_hash)
    }
    headers = {"Content-type": "application/json", "Accept": "text/plain", "user-agent": "git-hook"}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code != 200:
        print(f"the code review failed with the following error: {response.text}")
        exit(1)
    else:
        filename = f"./response_${commit_hash}.md"
        with open(filename, "w") as f:
            f.write(response.text)
        print(f"the file ${filename} will be created with your early"
            f"code review, please take a look at it before committing your code")
        exit(0)


codereview(commit_message, commit_code_changes, files_changed, commit_hash)
