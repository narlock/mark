# Mark

[![Latest Release](https://img.shields.io/github/v/release/narlock/mark)](https://github.com/narlock/mark/releases/)
[![Latest Commit](https://img.shields.io/github/last-commit/narlock/mark)](https://github.com/narlock/mark/commits/main)
[![Discord](https://discordapp.com/api/guilds/821757961830793236/widget.png?style=shield)](https://discord.gg/eEbEYbXaNS)

`mark` is a free, open source terminal-based website bookmark manager. Intended to help enhance a terminal-user's workflow.

## 🚀 Features

### 💾 Save a bookmark
Save a web bookmark using `mark <bookmark_name> <http_url>` to save a bookmark!

Example usage:
```sh
mark github https://github.com
Bookmark 'github' saved successfully!
```

### 📍 Open a saved bookmark
Open a saved bookmark in your web browser using `mark <bookmark_name>`. This will open your saved bookmark in your web browser!

Example usage:
```sh
mark github
Opening github...
```
and will open the "github" bookmark in the web browser.

## 📦 Installation

> [!IMPORTANT]  
> Currently, the installation script is only functional for Linux and Mac systems.

### 🐧 Linux / 🍎 macOS
1. Clone the [repository](https://github.com/narlock/mark). After cloning, navigate to the repository in your terminal.
2. Ensure that the `install.sh` script has execute permissions: `chmod +x install.sh`
3. Run the `install.sh` script: `./install.sh`. You will see the output in your terminal:

```
Installing Mark Bookmark Manager...
🚀 Installation complete! Use 'mark' to begin.
```

You have successfully installed `mark` to your machine. The contents of the installation were moved to the `$HOME/Documents/narlock/mark` directory, and a wrapper has been created inside of the `/usr/local/bin` directory to allow the `mark` command to be executed in your terminal.

### 🗑️ Uninstalling

On Linux / macOS systems, simply run the `uninstall.sh` script. You may need to grant execute permissions similar to the install script.

## 🗺️ Roadmap
The following section contains a list of features that will be implemented to enhance `mark`.
1. Allow the user to remove a bookmark from `mark` using `mark -r <bookmark_name>`. This will delete the bookmark entry from the config.txt file.
2. Allow bookmark "groups" to be created. A bookmark can be a part or not a part of a group. The user will be able to open all of the bookmarks in a group. The user will also be able to view all of the bookmarks in a group and remove bookmarks from a group.
3. Create a Windows installation option.
4. Implement a bookmark syncing feature. This will allow users of `mark` to sync bookmarks based on a "source of truth" system. This will most likely be done through LAN system, where a single system has ssh enabled. Systems that want to sync with that system can use some command to sync and the sync process will begin. Bookmarks that exist on synced devices will be saved to the source system and bookmarks that do not exist on the source system will be added from user systems.