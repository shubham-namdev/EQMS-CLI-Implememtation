import os


def clear():
    os.system('cls')

def color(col : str) -> None:
    if col == 'blue':
        os.system('color 1')
    elif col == 'red':
        os.system('color 4')
    elif col == 'green':
        os.system('color 2')
    elif col == 'white':
        os.system('color 7')
    elif col == 'aqua':
        os.system('color 3')
    else:
        os.system('color 7')