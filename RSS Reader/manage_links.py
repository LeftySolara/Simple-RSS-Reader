# functions to manage saved links

from sys import exit
from reader import main_menu
    

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