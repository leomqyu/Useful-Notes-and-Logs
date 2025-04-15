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

   To use, create at the machine that want to connect from, then copy the public key to the machine that want to connect to

2. connect with keys
    ```
    ssh -i <path_to_private_key> ...
    ```

3. copy private key to other machine:
    ```
    # first just copy the file to new machine
    ssh-agent bash
    ssh-add <path_to_copied_private_key>
    ```