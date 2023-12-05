#!/usr/bin/env python

from subprocess import check_output
log = check_output(['git', 'log', '-1', '--stat', 'HEAD'])

diff = check_output(['git', 'diff', '--stat', 'HEAD^', 'HEAD'])

commit_message = log.decode('utf-8').split('\n')[4]
commit_description = log.decode('utf-8').split('\n')[6]
commit_code_changes = diff.decode('utf-8').split('\n')[4:-1]

print(commit_message)
print(commit_description)
print(commit_code_changes)
