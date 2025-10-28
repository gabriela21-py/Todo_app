def get_todos(filepath="todos.txt"):
    """ Read a text file and return a list of to do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write a list of items to do."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
