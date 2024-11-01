#!/bin/bash

############cse147
# conda activate rnafm
# model_relative_path="1_train_on_HeLa/results/models/epoch=51-val_loss=0.61.ckpt"
# bash "/data2/mqyu/work/utils/notes/lightning/test_code/HeLa_cross_tissue_test_wb/1_train_on_HeLa/2_test.sh" cse147 $model_relative_path
#############

echo "testing"

server=$1
model_relative_path=$2

if [ "$server" = 'cse177' ]; then
    exit -1
    # data_dir="/data/project/mqyu/work/rna_mod/new_ds/128_0.8_only/final_results_w_neg/12_5fold/crossfold_128_HeLa_0.80_1to1"
    # work_base="/data/project/mqyu/work/rna_mod/new_model/wb_final_model_f${fold}"
elif [ "$server" = 'cse147' ]; then
    data_dir="/data2/mqyu/work/utils/notes/lightning/test_code/data"
    work_base="/data2/mqyu/work/utils/notes/lightning/test_code/HeLa_cross_tissue_test_wb"
else
    echo "unknown server, exit!"
    exit -1
fi

sources=("HEK293T" "Huh7" "A549" "iSLK")
sources=("HEK293T")

cd "${work_base}/1_train_on_HeLa"

for source in "${sources[@]}"; do
    rm -r "${work_base}/1_train_on_HeLa/results/${source}_result"
    mkdir -p "${work_base}/1_train_on_HeLa/results/${source}_result"

    echo "tesing $source"

    test_dir="/data2/mqyu/work/new_ds/128_0.8_only/final_results_w_neg/12_5fold/crossfold_128_${source}_0.80_1to1"
    test_fasta="${test_dir}/all_seq.fasta"
    # echo $test_fasta

    # if no complete test dir, concat train_no_val and test
    if [ ! -f "$test_fasta" ]; then
        echo "generating test_fasta file from scratch ..."

        train_no_val_fasta="/data2/mqyu/work/new_ds/128_0.8_only/final_results_w_neg/12_5fold/crossfold_128_${source}_0.80_1to1/fold0_no_val_train.fasta"
        test_no_train_fasta="/data2/mqyu/work/new_ds/128_0.8_only/final_results_w_neg/12_5fold/crossfold_128_${source}_0.80_1to1/fold0_test.fasta"

        cp $train_no_val_fasta $test_fasta
        cat $test_no_train_fasta >> $test_fasta
    fi

    # nohup python "${work_base}/1_train_on_HeLa/cross_source_test.py" \
    #         --work_base $work_base \
    #         --source $source \
    #         --test_dir $test_dir \
    #         --model_path $model_relative_path \
    #         --gpu 0 1 \
    #         --seq_len 128 \
    #         --batch_size 32 \
    #     > "${work_base}/1_train_on_HeLa/results/${source}_result/log.out" 2>&1 &

    python "${work_base}/1_train_on_HeLa/cross_source_test.py" --work_base $work_base --source $source --test_dir $test_dir --model_path $model_relative_path --gpu 0 1 --seq_len 128 --batch_size 32
    
done

