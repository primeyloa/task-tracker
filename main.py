# The program begins with a menu showing available actions and how and what commands to enter
# Program runs a while loop until user enters command to end program
# I want to desist from opening the file on the onset and maintaining it till the program ends, and instead open and close after every function call/execution
"""Receiving user inputs:
1. User can and will use positional arguments eg. 1, 2, 3 as per the menu that is shown
2. Commands preceed the user's additional input
3. User input is parsed separately from the preceeding command and fed to the complimetary function
"""

from modules.add import add_task


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
        # The main loop where actions can be done
        user_result = str(input("Action:> "))
        content = user_result.split(
            " "
        )  # converting the string commands to an array in order to ascertain command
        match content[0]:
            case "list":
                break

            case "add":
                task = str(content[1:])
                task = task.replace(task[0:2], "")
                task = task.replace(task[-2:], "")
                task = task.strip()
                add_task(task)
                break

            case "update":
                break

            case "delete":
                break

            case "mark-done":
                break

            case "mark-in-progress":
                break

            case "end":
                RUN_PROGRAM = False
                break

            case _:
                RUN_PROGRAM = True
        print("> Type in a command")
    print("Program has ended")


main()
