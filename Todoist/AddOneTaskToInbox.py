#!/usr/bin/env python3

from todoist_api_python.api import TodoistAPI

import sys 
api = TodoistAPI('yourTodoistApiCode')

try:
    task = api.add_task(content=sys.argv[1])
except Exception as error:
    print(error)