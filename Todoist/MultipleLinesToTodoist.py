#!/usr/bin/env python3

# Import necessary packages 
# sys for input arguments
# tkinter for userinterface and project selection
# todoist for Todoist Rest API

import sys 
import tkinter as tk
from tkinter import *
from todoist_api_python.api import TodoistAPI

# Setup Todoist Settings 
api = TodoistAPI('yourApi')
# If ypu want to display only one project and its subproject change here the settings 
targetProjectID = 2262951637
onlyTargetProjects = True  # Set to False if you want to display all projects

# initialise needed variables 
targetList = []
targetListsIds = []
result = None

# get all projects
try:
    projects = api.get_projects()
except Exception as error:
    print(error)

# save the selected projects to display them in the UI 
for project in projects:
    if onlyTargetProjects: 
        if project.id == targetProjectID or project.parent_id == targetProjectID:
            targetList.append(project.name)
            targetListsIds.append(project.id)
    else: 
            targetList.append(project.name)
            targetListsIds.append(project.id)
    if project.name == "Inbox": 
        inboxID = project.id

# initialise the userinterface input form with tKinter
root = tk.Tk()
items = tk.StringVar(value=targetList)
root.title('Project selection')

def select(event):
    lb.curselection()[0]
    
def exit_gui(event):
    global result
    for i in lb.curselection():
        result = i
    root.destroy()

# exit the ui by pressing return and return the selected project
root.bind("<Return>",exit_gui)

lb = tk.Listbox(root, listvariable=items, width=40, selectmode='browse')
lb.grid()
lb.bind('<<ListboxSelect>>', select)
lb.selection_set(0)
lb.focus_set()
lb.focus()

root.mainloop()

# save the selected project ID. If missing use the inbox instead
if result is not None: 
    projectid= targetListsIds[result]
else: 
     projectid = inboxID

# Split the input text by new line seperator and create for each line a task in the selected project
try:
    todo = sys.argv[1].splitlines() 
    for i in todo:
        task = api.add_task(content=i, project_id=projectid)
except Exception as error:
    print(error)