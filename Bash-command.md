# Bash command shortcuts

By default Readline uses emacs key bindings.

# Command Editing Shortcuts

- `Ctrl + a`: go to the start of the command line
- `Ctrl + e`: go to the end of the command line
- `Ctrl + k`: delete from cursor to the end of the command line
- `Ctrl + u`: delete from cursor to the start of the command line
- `Ctrl + w` or `Ctrl + x and then Backspace`: delete from cursor to start of word (i.e. delete backwards one word)
- `Ctrl + y`: paste word or text that was cut using one of the deletion shortcuts (such as the one above) after the cursor
- `Alt + b`: move backward one word (or go to start of word the cursor is currently on)
- `Alt + f`: move forward one word (or go to end of word the cursor is currently on)
- `Alt + d`: delete to end of word starting at cursor (whole word if cursor is at the beginning of word)

# Command Control Shortcuts

- `Ctrl + l`: clear the screen
- `Ctrl + s`: stops the output to the screen (for long running verbose command)
- `Ctrl + q`: allow output to the screen (if previously stopped using command above)
- `Ctrl + z`: suspend/stop the command
    - `fg {process_name}`: get the process back to the foreground
- `Ctrl + d`: exit the bash shell (same as running the exit command).
- `Ctrl + c`: terminate the command