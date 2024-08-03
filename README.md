# tmux-for-neteng
Example tmux configuration designed for Network Engineers

Special shoutout to https://leanpub.com/the-tao-of-tmux/read which was a major help in building this configuration. A great resource if you want to learn everything there is to know about tmux and want to build your own configuration.

## Installation

Pretty much every modern linux distribution these days has tmux installed by default. If not simply install tmux using your distributions package manager

To use this tmux configuration, simply copy and paste the contents of the .tmux.conf file into your home directories .tmux.conf

I've included an example addition to your .bashrc (example-bashrc.txt) which you can simply paste at the bottom of your .bashrc file and edit as necessary.

I've also included an example CSV file (hosts.csv) and accompanying basic python script to generate the .bashrc additions that you can use for your environment(s).

Remember to create the log directory in your home directory if you want automatic logging on your SSH sessions (mkdir log). Aliases are there so you can tab complete hosts with ease.

## Usage

TMUX should automatically start when you SSH into your host, but if not you can simply execute `source .bashrc`

Keybindings I've used as a personal preference, you can change this if you want in your own .tmux.conf file to suit your own preferences.

| Keybind | Description |
| --- | --- |
| `Ctrl+Space + c` | Create new window |
| `Ctrl+Space + Ctrl+Space` | Switch between current and last window (can hold down Ctrl) |
| `Ctrl+Space + 1-9` | Switch to window # |
| `Ctrl+Space + [` | Switch to scrollback mode, can use VIM bindings here to search, etc. Press Enter twice to exit |
| `Ctrl+Space + -` | Create a Horizontal Split |
| `Ctrl+Space + =` | Create a Vertial Split |
| `Alt+Arrow Keys` | Navigate between Split Panes |
| `Ctrl+Space + d` | Detach TMUX |
| `Ctrl+Space + r` | Reload TMUX config |

## Screenshots