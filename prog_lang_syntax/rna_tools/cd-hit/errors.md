# Fatal Error: in diag_test_aapn, MAX_DIAG reached

```
================================================================
Program: CD-HIT, V4.8.1 (+OpenMP), Nov 12 2024, 10:35:24
Command: cd-hit -i ./results/rna_seqs.fasta -o
         ./results/rna_clust/rna_thr=0.90.fasta -c 0.90 -n 5 -M
         0 -T 0

Started: Sat Nov 23 21:58:44 2024
================================================================
                            Output                              
----------------------------------------------------------------
total number of CPUs in the system is 64
Actual number of CPUs to be used: 64

total seq: 599278

Warning:
Some seqs are too long, please rebuild the program with make parameter MAX_SEQ=new-maximum-length (e.g. make MAX_SEQ=10000000)
Not fatal, but may affect results !!

longest and shortest : 1338345 and 18
Total letters: 4787963259
Sequences have been sorted

Approximated minimal memory consumption:
Sequence        : 4868M
Buffer          : 64 X 308M = 19728M
Table           : 2 X 74M = 149M
Miscellaneous   : 7M
Total           : 24754M

Table limit with the given memory limit:
Max number of representatives: 281250
Max number of word counting entries: 18446744073629803412

# comparing sequences from          0  to       9079

Fatal Error:
in diag_test_aapn, MAX_DIAG reached
Program halted !!
```

## solution

```
wget https://github.com/weizhongli/cdhit/releases/download/V4.8.1/cd-hit-v4.8.1-2019-0228.tar.gz
tar xvf cd-hit-v4.8.1-2019-0228.tar.gz --gunzip
cd cd-hit-v4.8.1-2019-0228
change the MAX_SEQ in cdhit-common.h to large enough (eg 10000000)
make
export to $PATH
```