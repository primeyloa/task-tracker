### Task Tracker application:
This is a python based CLI application that mimics terminal commands to access a simple json based storage for tasks. 
You can create, update, read and delete tasks. 
You see what I did there.... CRUD 
XD.... O__O 
##### These are some of the commands you can make:
---
- 'list':
  - 'list': This command lists all tasks stored.
  - 'list done': This command lists all tasks that are marked `'done'`.
  - 'list todo': This command lists all tasks marked `'to-do'`
  - 'list in-progress': This command lists all tasks marked `'in-progress'`
---
- 'add <`argument`>':
  - This command is followed by a string containing the textual information of the task you want to accomplish
---
- 'update <`argument`>': 
  - This command is followed by a number corresponding to the id of the task you want to update. Be it a task in progress, marked todo or done.
---
- 'delete <`argument`>':
  - This command is followed by a number corresponding to the id of the task you want to delete.
---
- 'mark':
  - 'mark-in-progress <`argument`>': This command marks tasks with the id given as an argument as 'in-progress'
  - 'mark-todo <`argument`>': This command marks a task with task id given as argument as 'todo'
  - 'mark-done <`argument`>: This command marks a task with given task id as 'done'

##### I added the functions as modules and imported them. I thought it would be cool and make the code readable.

> ***And oh, I did this md by myself too.*** 

$$
Kamikaze.
$$
https://roadmap.sh/projects/task-tracker 


