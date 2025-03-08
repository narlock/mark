"""
Mark - main.py
author: narlock

The beginning of the Mark bookmark manager application.
"""

import sys
import webbrowser
import datastore

# DEV INFO
GITHUB_LINK = "https://github.com/narlock"
GITHUB_REPO_LINK = "https://github.com/narlock/mark"
VERSION = 'v1.0.0'

# COMMAND INFO
VERSION_CMD = '-version'
LIST_CMD = '-list'

# ANSI Color Codes
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

def show_help():
    """Displays the available commands."""
    print(f"{CYAN}Mark Bookmark Manager - Created by: \033]8;;{GITHUB_LINK}\033\\narlock\033]8;;\033\\{RESET}")
    print("Usage: mark [options]\n")
    print("Where options include:\n")
    print("\t<bookmark_name>              Open saved bookmark in web browser.")
    print("\t<bookmark_name> <http_url>   Save a new bookmark.")
    print("\t-version                     Show current mark version.")
    print("\t-list                        List all saved bookmarks.")
    print(f"\nView usage demonstration on \033]8;;{GITHUB_REPO_LINK}\033\\GitHub\033]8;;\033\\.")

def show_version():
    """Displays the application version."""
    print(f"{CYAN}Mark Bookmark Manager - {VERSION}{RESET}")
    print(f"Check \033]8;;{GITHUB_REPO_LINK}\033\\GitHub\033]8;;\033\\ for the most up-to-date version.")

def open_bookmark(bookmark_name):
    """Opens a bookmark in the web browser if it exists."""
    bookmarks = datastore.load_bookmarks()
    if bookmark_name in bookmarks:
        print(f"{GREEN}Opening {bookmark_name}...{RESET}")
        webbrowser.open(bookmarks[bookmark_name])
    else:
        print(f"{RED}Error: Bookmark '{bookmark_name}' not found.\n\t Use {RESET}`mark -list`{RED} to view saved bookmarks!{RESET}", file=sys.stderr)


def save_bookmark(bookmark_name, http_link):
    """Saves a new bookmark to the config file."""
    if not http_link.startswith("http://") and not http_link.startswith("https://"):
        http_link = "https://" + http_link  # Ensure correct URL format
        
    datastore.save_bookmark(bookmark_name, http_link)
    print(f"{GREEN}Bookmark '{bookmark_name}' saved successfully!{RESET}")


def list_bookmarks():
    """Lists all saved bookmarks."""
    bookmarks = datastore.load_bookmarks()
    if not bookmarks:
        print(f"{RED}No bookmarks saved.{RESET}")
    else:
        print(f"{CYAN}Saved Bookmarks:{RESET}")
        for name, link in bookmarks.items():
            print(f"  {GREEN}{name}:{RESET} {link}")

def main():
    args = sys.argv[1:]

    if not args:
        # If no arguments are provided, the help menu will be printed to the terminal.
        show_help()
    elif args[0] == VERSION_CMD:
        # If the version command is provided, the version will be printed to the terminal.
        show_version()
    elif args[0] == LIST_CMD:
        # If the list command is provided, the list will be printed to the terminal.
        list_bookmarks()
    elif len(args) == 1:
        # mark <bookmark_name> - opens the bookmark.
        open_bookmark(args[0])
    elif len(args) == 2:
        # mark <bookmark_name> <http_url> - saves the bookmark.
        save_bookmark(args[0], args[1])
    else:
        print(f"{RED}Invalid command. Use {RESET}'mark'{RED} to see available options.", file=sys.stderr)


if __name__ == '__main__':
    main()
