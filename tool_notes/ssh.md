# Using private key to login to a server (so no need to use password)

https://www.cloudbolt.io/blog/linux-how-to-login-with-a-ssh-private-key/


# SSH alive

Alive
ssh -o ServerAliveInterval=60 user@host

或者

如果您希望在 SSH 配置文件中全局启用 keep-alive，可以将以下行添加到 ~/.ssh/config 文件中：
ServerAliveInterval 60


# SSH with keys

1. create a pair of key:
   ```
   ssh-keygen -t ed25519
   ```

   To use, create at the machine that want to connect FROM (local computer), 
   
1. copy the public key to the machine that want to connect to (remote server)

just copy the content in the `~/.ssh/id_rsa_xxx.pub` of local machine to the file with the same name in te folder `.ssh/authorized_keys` the remote machine

2. connect with keys
    ```
    ssh -i <path_to_private_key> ...
    ```

    (In vscode, if use ssh key, some times need to open ssh configuration file and change "IdentityFile" to the correct file path)

3. copy private key to other machine (try to avoid):
    ```
    # first just copy the file to new machine
    ssh-agent bash
    ssh-add <path_to_copied_private_key>
    ```