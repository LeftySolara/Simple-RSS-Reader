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
    print()
    return filename


def main_menu(filename,links):
    print("1. Read feeds\n2. Add feeds\n3. Remove Feeds\n4. Exit")
    option = input("> ")
    print()
    if option == '1':
        pass
    elif option == '2':
        manage_links.add_links(filename,links)
    elif option == '3':
        manage_links.remove_links(filename,links)
    elif option == '4':
        exit(0)
    links = manage_links.get_links(filename)
    return links


def print_feed_names(links):
    print("Subscribed Feeds:\n")
    i = 0
    for name in links:
        myfeed = feedparser.parse(name)
        print("{}) {}".format(i,myfeed.feed.title))
        i += 1
    print()


def display_feed(feed_num,links):
    try:
        mylink = links[int(feed_num)]
        myfeed = feedparser.parse(mylink)
        print()
        print(myfeed.feed.title)
        print(myfeed.feed.description)
    except IndexError:
        print("Feed not found.")


def main():
    filename = welcome()
    links = manage_links.get_links(filename)
    links = main_menu(filename,links)
    print_feed_names(links)
    feed_num = input("Enter number of feed to display: ")
    display_feed(feed_num,links)

if __name__ == "__main__":
    main()