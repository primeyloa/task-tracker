import json


def add_task(user_input):
    """For adding task, we use the file system operation to add content to the file storing
    information about tasks.
    """
    content = user_input
    assert type(content) is str
    with open(
        "tasks.json", "a"
    ) as f:  # using action 'a' to append to file and avoid overwriting
        task = content + "\n"
        file = json.load(f)
        print(file.keys())
        task_obj = {"id": 1, "task": task}
        try:
            # f.write(json_obj)
            json.dump(task_obj, f)
            print("Task added successfully!")
        except Exception:
            print("The file could not be modified")
