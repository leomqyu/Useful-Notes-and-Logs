# Using private key to login to a server (so no need to use password)

https://www.cloudbolt.io/blog/linux-how-to-login-with-a-ssh-private-key/


# SSH alive

Alive
ssh -o ServerAliveInterval=60 user@host

或者

如果您希望在 SSH 配置文件中全局启用 keep-alive，可以将以下行添加到 ~/.ssh/config 文件中：
ServerAliveInterval 60
