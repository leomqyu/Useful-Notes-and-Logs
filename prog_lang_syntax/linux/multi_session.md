
# tmux
## intro  
create several "pseudo terminals" (*"sessions"*) from a single terminal  
Tmux also decouples your programs from the main terminal. You can detach tmux from the current terminal, and all your programs will continue to run safely in the background. Later, you can reattach tmux to the same or a different terminal.

## general
```bash
tmux ## create a tmux window
## do things as usual
Ctrl+B, D   ## detach
```


## basic tmux commands
```bash
tmux                         ## start new
tmux new -s myname           ## start new with session name
tmux a                       ##  (or at, or attach)
tmux a -t myname             ## attach to named
tmux ls                      ## list sessions
tmux kill-session -t myname  ## kill session
tmux kill-server
tmux switch -t <session-name>   ## switch session
tmux rename-session -t 0 <new-name> ## rename session
```

## key bindings

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


# screen

## Intro  

Similar to `tmux`:  
Can launch and use multiple shell sessions from a single ssh session.   
When a process is started with ‘screen’, the process can be detached from session & then can reattach the session at a later time.  
When the session is detached, the process that was originally started from the screen is still running and managed by the screen itself.  
The process can then re-attach the session at a later time, and the terminals are still there, the way it was left.

## Create window

```
screen -S <window_name>
```

## Inspect

1. inspect all the windows, attached and detached
    ```
    screen -ls
    ```

## Attach and detach window

1. detach
    1. Use Ctrl (a + d)
    2. `screen -d <window_name>`
   
1. reattach
    `screen -r <window_name>`

## Close 

1. type `exit` in the window
2. Ctrl (a + k)
   

## Full example

1. start a screen window 
   ```
   screen -S sample_screen
   ```

2. Assume to run a forever running process
    ```
    #!/bin/bash

    counter=0

    while true; do
        echo "Counter: $counter"
        counter=$((counter + 1))
        sleep 3
    done
    ```

3. To detach and log out, do Ctrl (a + d)
    Note: no need to have the process run on background, just detach and it will run as file

4. When back and check the process: 
    `screen -r sample_screen`