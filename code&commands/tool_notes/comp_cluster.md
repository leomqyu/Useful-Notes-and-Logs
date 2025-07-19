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

# Use jupyter notebook on clusters' computational nodes (in vscode)
1. BG: when you go to a cluster, all you're doing and all vscode can access is the log-in node. But sometimes we want the jupyter notebook to run in computation nodes
1. reference: https://advancedsolvercluster.github.io/guide/software/python/python-jupyter-notebook