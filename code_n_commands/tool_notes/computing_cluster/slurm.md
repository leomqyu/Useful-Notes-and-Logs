# intro
a job scheduler, submit jobs to it, it manages the queue and push the jobs to the computer clusters

# terminologies
## clusters
1. High Performance Computing (HPC)  
2. RONIN on AWS: ? a way to organize remote machines  
3. machine, virtual machine, hypervisor, instance (a machine created in the cloud on AWS)

## CPUs
1. nowadays CPUs can have multi core, each core run prog idpd
2. can run diff threads of a process on multiple cores of a CPU. If only have one core, can make virtual CPUs as if multi core: Simultaneous MultiThreading (SMT) or hyperthreading (Intel).

## cluster  
1. A cluster is a collection of machines that are connected
2. don't run on a big cloud machine, but create a cluster of small machines
3. cluster can auto-scaling with minimum and a maximum number of nodes to bound
4. One of the biggest advantages of running a cluster in the cloud is the ability to easily scale up or scale down the size of your cluster as needed
5. Each machine (or instance) in a cluster is called a node;  A cluster is structured so that one node, the head node, controls the cluster. The remaining worker nodes are compute nodes.
6. CPUs can be virtual
7. on a cluster, user write a script to "submit" it to a scheduler (software that runs on the nodes of a cluster) that decides if and where it can be run. can be waiting in a queue.

# sbatch
0. [reference](https://docs.erc.monash.edu/M3/RunningJobsOnM3/BatchJobs)

1. eg usage
   1. script
        ```
        #!/bin/bash
        #SBATCH --job-name="Example job name!"
        #SBATCH --time=1:00:00
        #SBATCH --cpus-per-task=1
        #SBATCH --mem=1G

        echo "This job has started!"
        sleep 10
        echo "This job has ended!"
        ```
    1. submit
        to run the script, `sbatch my-script.slurm` to add it to a queue (the current command ends immediately)

# srun
1. intro: more useful. Basically used with tmux / screen to simulate: as if directly running.

1. eg:
    just open a tmux session and run it inside
    ```
    srun --mem=1G --cpus-per-task=1 --time=1:00:00 --partition=gpu --gres=gpu:1 --pty bash
    ```

# using python notebook on computational node and managing it on the vscode of log-in node
1. on the log-in node, use srun to go to the comp node
    ```
    srun --job-name srunbash --mem=1G --cpus-per-task=1 --time=10:00:00 --partition=gpu --gres=gpu:1 --pty bash
    ```
1. set up a jupyter notebook (by using ip=0.0.0.0, all nodes can access, no port forwarding needed) (or start it in a screen session): 
    ```jupyter notebook --no-browser --port=55555 --ip=0.0.0.0```
1. jot down the URL from jupyter notebook, that NOT start with the localhost, eg http://m3g111:55555/api/kernels/2f7288b9-e9ea-4865-be8b-7274d88f23dd...
1. open the vscode and on the top right corner of “select server”, choose “existing jupyter server” and paste in the URL in step 3. then can function
