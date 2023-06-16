# from functions import get_todos, write_todos
from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
TODOS_FILE = "todos.txt"

print("It is",now)

while True:
    user_action = input("Type add, show, edit, complete or exit:").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos(TODOS_FILE)

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show') or user_action.startswith('display'):
        todos = functions.get_todos(TODOS_FILE)

        for index, item in enumerate(todos):
            item = item.strip('\n')
            display = f"{index+1}: {item}"
            print(display)
    elif user_action.startswith('edit'):
        try:
            editID = int(user_action[5:])
            editID = editID - 1

            todos = functions.get_todos(TODOS_FILE)

            todo = input("What is the new value?")
            todos[editID] = todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos(TODOS_FILE)

            id_to_complete = int(user_action[9:])
            completed_todo = todos[id_to_complete - 1].strip('\n')

            if todos[id_to_complete - 1]:
                todos.pop(id_to_complete - 1)

            functions.write_todos(todos)

            print(f"Todo {completed_todo} is now complete")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print(user_action + " is an unknown command")

print('bye')
