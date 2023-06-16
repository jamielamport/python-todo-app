FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a test file and return the
    list of todo items
    """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath=FILEPATH):
    """ Read the current todos from a file, add our new
    todo and then write back to the file
    """
    with open(filepath, "w") as file:
        file.writelines(todos)

if __name__ == "__main__":
    print(get_todos())
