import os

def walk(dirname):
    """
    Prints the names of all files in dirname and its subdirectories.
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


def walk2(dirname):
    """
    Prints the names of all files in dirname and its subdirectories.
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))



folder = '.'

walk(folder)
#walk2(folder)
