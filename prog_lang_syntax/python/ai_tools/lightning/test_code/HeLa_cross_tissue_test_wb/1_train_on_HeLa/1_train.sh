############cse147
# conda activate rnafm
# bash "/data2/mqyu/work/utils/notes/lightning/test_code/HeLa_cross_tissue_test_wb/1_train_on_HeLa/1_train.sh" cse147       
#############

server=$1

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


cd "${work_base}/1_train_on_HeLa"
rm -r /data2/mqyu/work/utils/notes/lightning/test_code/HeLa_cross_tissue_test_wb/1_train_on_HeLa/results
mkdir -p "${work_base}/1_train_on_HeLa/results"

echo "here testing"

python "${work_base}/1_train_on_HeLa/train_mul_gpu.py" \
                                    --work_base "${work_base}" \
                                    --data_dir "${data_dir}" \
                                    --gpu 0 1 \
                                    --seq_len 128 \
                                    --batch_size 1 --lr 1e-3 --weight_decay 1e-4 \
                                    --epochs 70 --save_every 1

