FILEPATH = "todos.txt"


def get_todos(file_path=FILEPATH):
    """Read a text file and return the list of
    to-do items
    """
    with open(file_path,
              "r") as file:  # with context manager automatically close the file when file operation are completed
        todo = file.readlines()
    return todo


def write_todos(todo_arg, filepath=FILEPATH):
    """Write a to-do item from a list in a text file"""
    with open(filepath, "w") as file:
        file.writelines(todo_arg)


def print_ls(ls):
    for idx, todo_el in enumerate(ls):  # enumerate return index and item
        todo_el = todo_el.capitalize()
        elem = todo_el.strip('\n')
        todo_row = f"{idx + 1}-{elem}"  # Use fstrings method in order to remove the space between the idx and todo_el
        # print(idx, '-', todo_el)
        print(todo_row)
    print('')


if __name__ == "__main__":  # __main__ is the name assigned to functions.py when you run only this function.
    print("hello functions")
