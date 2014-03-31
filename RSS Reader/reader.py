# feed reader (WIP)

import feedparser
import manage_links
import file_ops
from os.path import isfile

def welcome():
    print("-- RSS Feed Reader --\n")
    file_ops.show_files()
    dir_option = input("Use this directory(Y/N)? ")
    while dir_option.upper() != 'Y':
        try:
            file_ops.change_dir()
            dir_option = input("Use this directory(Y/N)? ")
        except FileNotFoundError:
            print("Directory not found.")
    filename = ''
    while not isfile(filename):
        filename = input("Enter feed file: ")
        if not isfile(filename):
            print("File not found")
    return filename

def main_menu(filename,links):
    print("1. Read feeds\n2. Add feeds\n3. Remove Feeds\n4. Exit")
    option = input("> ")
    if option == '2':
        manage_links.add_links(filename,links)
        links = manage_links.get_links(filename)
    elif option == '3':
        manage_links.remove_links(filename,links)
        links = manage_links.get_links(filename)
    elif option == '4':
        exit(0)

def main():
    filename = welcome()
    links = manage_links.get_links(filename)
    main_menu(filename,links)

if __name__ == "__main__":
    main()