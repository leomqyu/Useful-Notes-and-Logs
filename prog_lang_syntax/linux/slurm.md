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