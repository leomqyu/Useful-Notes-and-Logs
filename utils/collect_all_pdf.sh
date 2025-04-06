src_dir="./umap_diff_hyprm_results"
out_dir="./_pdf_collect"

mkdir -p ${out_dir}
find $src_dir -type f -iname "*.pdf" -exec cp -n {} $out_dir \;