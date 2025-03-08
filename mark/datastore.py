"""
Mark - datastore.py
author: narlock

This file serves the purpose for interfacing with the datastore.
In this case, the datastore is a simple text file stored under:
Documents/narlock/mark/config.txt
"""

import os

CONFIG_PATH = os.path.expanduser('~/Documents/narlock/mark/config.txt')

def load_bookmarks():
    """Loads bookmarks from the config file."""
    if not os.path.exists(CONFIG_PATH):
        return {}

    bookmarks = {}
    with open(CONFIG_PATH, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(" ", 1)
            if len(parts) == 2:
                bookmarks[parts[0]] = parts[1]
    return bookmarks


def save_bookmark(bookmark_name, http_link):
    """Saves a new bookmark to the config file."""
    bookmarks = load_bookmarks()
    bookmarks[bookmark_name] = http_link
    save_bookmarks(bookmarks)


def save_bookmarks(bookmarks):
    """Saves bookmarks to the config file."""
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, 'w', encoding='utf-8') as file:
        for name, link in bookmarks.items():
            file.write(f"{name} {link}\n")