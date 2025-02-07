# intro  
create several "pseudo terminals" (*"sessions"*) from a single terminal  
Tmux also decouples your programs from the main terminal. You can detach tmux from the current terminal, and all your programs will continue to run safely in the background. Later, you can reattach tmux to the same or a different terminal.

# general
```bash
tmux # create a tmux window
# do things as usual
Ctrl+B, D   # detach
```


# basic tmux commands
```bash
tmux                         # start new
tmux new -s myname           # start new with session name
tmux a                       #  (or at, or attach)
tmux a -t myname             # attach to named
tmux ls                      # list sessions
tmux kill-session -t myname  # kill session
tmux kill-server
tmux switch -t <session-name>   # switch session
tmux rename-session -t 0 <new-name> # rename session
```

# key bindings

note sometimes is Ctrl+A  

terminologies: 
    session: a tmux 
    pane: the view. diff pane can same or diff window
    window: mul windows in a session, 

```
Ctrl+B D — Detach from the current session.
Ctrl+B % — Split the window into two panes horizontally.
Ctrl+B " — Split the window into two panes vertically.
Ctrl+B Arrow Key (Left, Right, Up, Down) — Move between panes.
Ctrl+B X — Close pane.
Ctrl+B C — Create a new window.
Ctrl+B N or P — Move to the next or previous window.
Ctrl+B 0 (1,2...) — Move to a specific window by number.
Ctrl+B : — Enter the command line to type commands. Tab completion is available.
Ctrl+B ? — View all keybindings. Press Q to exit.
Ctrl+B W — Open a panel to navigate across windows in multiple sessions.

Ctrl+D or exit: exit
```