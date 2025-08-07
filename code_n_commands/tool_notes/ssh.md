# Using private key to login to a server (so no need to use password)

https://www.cloudbolt.io/blog/linux-how-to-login-with-a-ssh-private-key/

# SSH port forwarding
1. references: [ssh.com](https://www.ssh.com/academy/ssh/tunneling-example), [csdn post](https://blog.csdn.net/Gemini1995/article/details/144132124)
2. Intro: 
   SSH port forwarding is a mechanism in SSH for tunneling application ports from the client machine to the server machine, or vice versa. e.g. want the python notebook to run in computation nodes of a cluster, but want to manipulate the notebook to be manipulated in VSCode (which is only in log-in node). Then can forward the port of the computation node to the log-in node.
3. Local forwarding: 
    1. Intro
        forward a port from the client machine to the server machine, so that in the server machine, can ~ "go to websites that is on local machine" 
    1. Command Syntax
        ```
        ssh -L [local_address]:[local_port]:[remote_address]:[remote_port] [remote_host]
        ```
        This forwards traffic from your local machine (where you run the command) on local_address:local_port to remote_address:remote_port through remote_host.
    1. eg
        1. Write in the terminal of the local machine:
            ```
            ssh -L 127.0.0.1:55555:127.0.0.1:55556 user@remote_host
            ```
            explanation:
            1. `127.0.0.1:55555:127.0.0.1:55556` is the port forwarding specification:
                1. 127.0.0.1 (local_address): Address local machine. Can omit, then it will by default be localhost
                2. 55555 (local_port): The port on local machine to listen for incoming connections.
                3. 127.0.0.1 (remote_address): Target address on the remote machine.
                4. 55555 (remote_port): The port on the remote machine to which the traffic will be forwarded.
            2. This forwards traffic from your local machine's port 55555 to the remote machine (which is user@remote_host)'s port 55555, effectively creating a secure tunnel between these two ports. As a result, eg when I access at the local machine's browser: `127.0.0.1:55555`, I am effectively accessing the `127.0.0.1:55556` on the remote machine of user@remote_host.
        2. bypass firewall
            ```
            ssh -L 1302:google.com:443  root@43.142.140.60
            ``` 
            When I go to `localhost:1302` on my own computer, I am actually seeing the info as I am accessing `google.com:443` on the machine of `43.142.140.60`
    1. other arguments
        `ssh -fN -L ...`: -fN flags to run SSH in the background (-f) and disable remote command execution (-N), keeping the tunnel open without logging in.

# SSH with keys

1. create a pair of key:
   ```
   ssh-keygen -t ed25519
   ```

   To use, create at the machine that want to connect FROM (local computer), 
   
1. copy the public key to the machine that want to connect to (remote server)

    `[WRONG]`: ~~(just copy the content in the `~/.ssh/id_rsa_xxx.pub` of local machine to the file with the same name in the folder `.ssh/authorized_keys` the remote machine)~~

    Note, in some machines, just copy the content of `id_rsa_xxx.pub` to a file named `~/.ssh/authorized_keys`.

    Other note:  
        - if not OK, sometimes possibly because of the file mode.

2. connect with keys
    ```
    ssh -i <path_to_private_key> ...
    ```

    (In vscode, if use ssh key, some times need to open ssh configuration file and change "IdentityFile" to the correct file path; for windows path, change `\` to `/`)

3. copy private key to other machine (try to avoid):
    ```
    # first just copy the file to new machine
    ssh-agent bash
    ssh-add <path_to_copied_private_key>
    ```

# SSH alive

Alive
ssh -o ServerAliveInterval=60 user@host

或者

如果您希望在 SSH 配置文件中全局启用 keep-alive，可以将以下行添加到 ~/.ssh/config 文件中：
ServerAliveInterval 60