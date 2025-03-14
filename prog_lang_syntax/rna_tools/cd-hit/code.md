# Clustering

## basic notes
cd-hit-est designed for nucleotide. But don't have too low threshold. 
cd-hit has lower possible threshold. Originally used for protein, can also use for RNA 
## sample cluster of RNA and protein (exactly the same)


```bash
#!/bin/bash

# 
# cd /data/project/mqyu/work/rna_mod/new_ds/data
# work_base=/data/project/mqyu/work/rna_mod/new_ds/data
# nohup bash /data/project/mqyu/work/rna_mod/new_ds/data/final_ppl_w_neg/5_cd_hit_cluster.sh $work_base > /data/project/mqyu/work/rna_mod/new_ds/data/final_results_w_neg/5_cluster_result/log/out.out 2>&1 &

work_base=$1

numbers=("128" "256")

files=("HeLa" "hESC-HEK293T" "HEK293" "brain" "HEK293A-TOA" "TREX" "endometrial" "H1A" "H1B" \
       "GM12878" "iSLK" "HEC-1-A" "HEK293T" "NB4" "Huh7" "LCLs" "fibroblasts" "A549" "hNPCs" \
       "MT4" "HepG2" "liver" "MSC" "Jurkat" "peripheral-blood" "GSC-11" "GSCs" "TIME" "MM6" \
       "hESCs" "U2OS" "CD4T" "AML" "H1299" "kidney" "CD8T" "CD34" "BGC823" "cytosolic")

thresholds=("0.90" "0.80" "0.70" "0.60" "0.50")
ns=(        "5"    "5"    "5"    "4"    "3")

input_dir="${work_base}/final_results_w_neg/4_fasta_each_cell_line_maybe_similar"
output_dir="${work_base}/final_results_w_neg/5_cluster_result"
log_dir="${output_dir}/log"

# rm -rf $output_dir                 
# mkdir -p $log_dir


# Loop through each number
i=0
total_len=$(( ${#numbers[@]} * ${#files[@]} * ${#thresholds[@]} ))
# echo $total_len
for number in "${numbers[@]}"; do
    # Loop through each file
    for file in "${files[@]}"; do
        # init
        input_fasta="${input_dir}/hg38_${number}_${file}.fa"

        for ((i=0; i<${#thresholds[@]}; i++)); do
            threshold="${thresholds[i]}"
            n="${ns[i]}"

            out_fasta="${output_dir}/rep_${number}_${file}_${threshold}.fasta"

            if [ -f "$out_fasta" ]; then
                echo "Output file $out_fasta already exists. Skipping..."
                continue
            fi

            log_path="${log_dir}/${threshold}.out"

            cd-hit -i "$input_fasta" -o "$out_fasta" -c "$threshold" -n $n -M 0 -T 0

            echo "stored in ${out_fasta}"
        done
    done
done

```

# Comparing 

## basic notes

Use ```ci-hit-2d``` (or ```ci-hit-est-2d```)

It identifies the sequences in db2 that are similar to db1 at a certain threshold. 
The input are two protein datasets (db1, db2) in fasta format 
the output are two files: a fasta file of proteins in db2 

eg command:
```bash
cd-hit-2d -i db1 -i2 db2 -o db2novel -c 0.9 -n 5
```
