# feed reader (WIP)

import feedparser
import manage_links
from os.path import isfile


def get_settings():
    settings = {}
    with open("RSS Reader/settings.txt",'r') as settings_file:
        for i in settings_file:
            line = i.replace('\n', '')
            index = line.find(':')
            if index != -1:
                setting = line[0:index]
                val = line[index+2:]
                settings[setting] = val
    return settings


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


def display_feed(feed_num,links,num_articles):
    try:
        mylink = links[int(feed_num)]
        myfeed = feedparser.parse(mylink)
        print()
        print(myfeed.feed.title)
        print(myfeed.feed.description)
        print()
        for i in range(0,num_articles):
            print("{}) {}".format(i,myfeed.entries[i].title))
    except IndexError:
        print("Feed not found.")
    print()



def main():
    print("-- RSS Feed Reader --\n")
    settings = get_settings()
    filename = settings["feed list"]
    num_articles = int(settings["number of articles"])
    links = manage_links.get_links(filename)
    links = main_menu(filename,links)
    print_feed_names(links)
    feed_num = input("Enter number of feed to display: ")
    display_feed(feed_num,links,num_articles)

if __name__ == "__main__":
    main()