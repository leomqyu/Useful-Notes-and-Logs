# Path

**Describe**
When you say run a command like `ls`, how does it know which exe is this `ls`? Just find the file in some collection of directories and search the name in these directories. These directories are stored (separated by `:`) in the `$PATH` variable.

1. show the path dirs  
   `echo $PATH`
1. temporarily modify $PATH:
    ```
    export PATH="/Directory1:$PATH"
    ```
1. permanently modify:
   add this export statement to the `~/.bashrc`

# bg, process
1.	Show process run by yourself: 
    ```
    ps -u mqyu
    htop -u mqyu commands 
    top -u mqyu -c
    ```
    
2.	Run in background:
    `nohup python 1_predict.py > nohup_out_1.out 2>&1 &`

    already running:

    `disown -a`
    `disown -h %1`

3.	See process:
    `jobs / w`

4.	Kill
    ```
    kill -9 PID
    killall -u mqyu
    kill -2 PID     # more warmly. Like CTRL+C (SIG_INT)
    ```

5. Inspect process by PID
    ```
    ps -p <PID> -o user,comm        # get the command and the user name
    ```

# OS related
1. See the size of a dir:
    `du -sb /path/to/directory`

# Connection
1. scp and file transfer

    `scp -P <port> -r work/rna_mod/model/data/ mqyu@some.address:~`

2. see ip address
   `ifconfig`

# Compress uncompress
1. compress  
    tar -czvf [archive name].tar.gz [pathtofile]
1. uncompress 
    tar -xzvf [file .tar.gz]

    zip file: unzip file.zip
    bed file: gunzip [file path]

# Configuration

1. set alias
    For temporary: just eg `alias ll='ls -lah'`
    For permanent: add `alias ll='ls -lah'` in `~/.bash.rc`

# Others
1. Find
    `find . -name thisfile.txt`