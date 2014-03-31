# functions to manage saved links

from sys import exit
import file_ops

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
    filename = input("Enter feed file: ")
    links = get_links(filename)
    main_menu(filename,links)

def main_menu(filename,links):
    print("1. Read feeds\n2. Add feeds\n3. Remove Feeds\n4. Exit")
    option = input("> ")
    if option == '2':
        add_links(filename,links)
        links = get_links(filename)
    elif option == '3':
        remove_links(filename,links)
        links = get_links(filename)
    elif option == '4':
        exit(0)
    
def add_links(filename,links):
    # add links to file
    new_feed = ''
    while new_feed.upper() != 'R':
        new_feed = input("Enter link for new feed or 'r' to return to menu: ")
        if len(new_feed) > 1:
            links.append(new_feed)
    with open(filename,'w') as file_obj:
        for i in links:
            file_obj.write(i + '\n')
    main_menu(filename,links)

def remove_links(filename,links):
    # remove links from file
    print("Current feeds:\n")
    for i in links:
        print(i)
    print()
    target = ''
    while target.upper() != 'R':
        target = input("Enter feed to remove or 'r' to return to menu: ")
        if target in links:
            links.remove(target)
        else:
            print("Link not found.")
    with open(filename,'w') as file_obj:
        for i in links:
            file_obj.write(i + '\n')
    main_menu(filename,links)

def get_links(filename):
    # reads feed links from file
    links = []
    link_file = open(filename,'r')
    for line in link_file:
        link = line.replace('\n', '')
        links.append(link)
    link_file.close()
    return links