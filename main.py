# The program begins with a menu showing available actions and how and what commands to enter
# Program runs a while loop until user enters command to end program
# I want to desist from opening the file on the onset and maintaining it till the program ends, and instead open and close after every function call/execution

import json
import os


def main():
    print("""
        Welcome to Task Tracker!
        These are some of the things you can do:
            Add, update and delete tasks.
            List all tasks, as well as specific ones based on status.
            Mark tasks as in progress or done!

            You can also type "end" to exit.
        """)

    RUN_PROGRAM = True  # This variable is what keeps the program running
    while RUN_PROGRAM:
        # The file is loaded again and again

        # The main loop where actions can be done
        user_result = str(input("Action:> "))
        content = user_result.split(
            " "  # split made by spacing - convenient
        )  # converting the string commands to an array in order to ascertain command

        match content[0]:
            case "list":
                # Format: list
                list_tasks()

            case "list-done":
                # Format: list-done
                list_done()

            case "list-in-progress":
                # Format: list
                list_in_progress()

            case "list-todo":
                # Format: list
                list_todo()

            case "add":
                try:
                    # Format: add "Go jogging"
                    task = ""
                    for i in range(1, len(content)):
                        task = task + " " + content[i]
                    task = task[2:-1]
                    print(task)
                    task = task.strip()
                    add_task(task)
                except Exception as e:
                    print("Task could not be added due to error: {}".format(e))

            case "update":
                # Format: update 1 "Add groceries"
                task_id = int(content[1])
                task = ""
                for i in range(
                    2, len(content)
                ):  # we use similar conventions from adding tasks, but here, we start from 2
                    task = task + " " + content[i]
                task = task[2:-1]
                print(task)
                task = task.strip()
                update_task(task_id, task)

            case "delete":
                # Format: delete 1
                task_id = int(content[1])
                delete_task(task_id)

            case "mark-todo":
                # Format: mark-todo 4
                task_id = int(content[1])
                mark_todo(task_id)

            case "mark-done":
                # Format: mark-done 2
                task_id = int(content[1])
                mark_done(task_id)

            case "mark-in-progress":
                task_id = int(content[1])
                mark_in_progress(task_id)

            case "end":
                RUN_PROGRAM = False
                break

            case _:
                RUN_PROGRAM = True

        print("> Type in a command")
    print("Program has ended")


file_name = "tasks.json"


def load_tasks():
    # Check if file exists and is not empty
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        return []  # Return an empty list so len(file) doesn't crash
    with open(file_name, "r") as file:
        # content = file.read()
        return json.loads(file.read())


def add_task(task):
    file = load_tasks()
    content = task
    content1 = "".join(content[0:])
    default_status = "todo"
    task_obj = {"id": len(file) + 1, "task": content1, "status": default_status}
    file.append(task_obj)
    print("Task added successfully!")
    return save_task(file)


def save_task(task):
    with open(file_name, "w") as file:
        json.dump(task, file, indent=4)


def update_task(task_id, task):
    file = load_tasks()
    try:
        for obj in file:
            if obj["id"] == task_id:
                obj["task"] = task
                # file.append(obj)
                save_task(file)
                print("Task updated successfully!")

    except Exception as e:
        print("Task could not be updated: {}".format(e))


def mark_todo(task_id):
    file = load_tasks()
    try:
        for obj in file:
            if obj["id"] == task_id:
                obj["status"] = "todo"
                # file.append(obj)
                save_task(file)
                print("Task updated successfully!")

    except Exception as e:
        print("Task could not be updated: {}".format(e))


def mark_in_progress(task_id):
    file = load_tasks()
    try:
        for obj in file:
            if obj["id"] == task_id:
                obj["status"] = "in-progress"
                # file.append(obj)
                save_task(file)
                print("Task updated successfully!")

    except Exception as e:
        print("Task could not be updated: {}".format(e))


def mark_done(task_id):
    file = load_tasks()
    try:
        for obj in file:
            if obj["id"] == task_id:
                obj["status"] = "done"
                # file.append(obj)
                save_task(file)
                print("Task updated successfully!")

    except Exception as e:
        print("Task could not be updated: {}".format(e))
    pass


def list_tasks():
    file = load_tasks()
    for obj in file:
        print("{} {}".format(obj["id"], obj["task"]))



def list_done():
    file = load_tasks()
    for obj in file:
        if obj["status"] == "done":
            print("{}. {}".format(obj["id"], obj["task"]))
    

def list_todo():
    file = load_tasks()
    for obj in file:
        if obj["status"] == "todo":
            print("{}. {}".format(obj["id"], obj["task"]))
    

def list_in_progress():
    file = load_tasks()
    for obj in file:
        if obj["status"] == "in-progress":
            print("{}. {}".format(obj["id"], obj["task"]))    


def delete_task(task_id):
    file = load_tasks()
    try:
        i = 0
        for obj in file:
            if obj["id"] == task_id:
                del file[i+1]
                save_task(file)
                print("Task deleted successfully!")
                i =+1
    except Exception as e:
        print("Could not delete task: {}".format(e))
    


if __name__ == "__main__":
    main()
