# file operation options

from os import listdir, chdir, getcwd
from os.path import isfile, isdir


def show_files():
    """ Displays files in current working directory """

    dir_list = listdir()
    print("In current directory:")
    for i in dir_list:
        index = dir_list.index(i)
        if isfile(i) == True:
            print("{:>3}: {}".format(index,i))
        elif isdir(i) == True:
            print("{:>3}: {}/".format(index,i))
    print("")


def change_dir():
    """ Changes current working directory. """

    print("Enter desired directory path:")
    path = input("> ")
    chdir(path)
    print("Directory changed to {}".format(getcwd()))
    print()
    show_files()