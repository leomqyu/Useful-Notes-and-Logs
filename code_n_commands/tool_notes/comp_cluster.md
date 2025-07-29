# basic bg knowledge
1. CPUs, cores, and sockets:
https://docs.erc.monash.edu/M3/RunningJobsOnM3/BatchJobs 
1. there will be different nodes in a cluster, eg computational nodes, login nodes ... when logged in, usually at the login node, use Slurm to "change" to different nodes

# commands
1. see node info
    ```
    sinfo       # show all nodes
    scontrol show config    # show cluster config
    squeue      # state of the jobs
    ```
2. see gpu info
    ```
    gpu:P4:6(S:0-1)
    ```

    sample output:
    ```
    NODELIST GRES
    m3h[100-101] gpu:H100:4(S:0-1)
    m3g[020-023] gpu:V100:3(S:0-1)
    ```

    format: `[node_names] gpu:[GPU_TYPE]:[COUNT](S:[SOCKET_IDS])`

3. allocate process
    1. detailed see MU MASSIVE doc
    2. common srun commands
        ```
        srun --job-name srunbash --mem=8G --cpus-per-task=1 --time=10:00:00 --partition=gpu --gres=gpu:A40:2 --pty bash
        srun --job-name srunbash --mem=8G --cpus-per-task=1 --time=10:00:00 --partition=gpu --gres=gpu:1 --pty bash		# specify GPU type
        srun --mem=1G --cpus-per-task=1 --time=10:00:00 --pty bash  # cpu only
        ```

# Use jupyter notebook on clusters' computational nodes (in vscode)
1. BG: when you go to a cluster, all you're doing and all vscode can access is the log-in node. But sometimes we want the jupyter notebook to run in computation nodes
1. reference: https://advancedsolvercluster.github.io/guide/software/python/python-jupyter-notebook