import os

# path="/home/sejung/Patch-NetVLAD/patchnetvlad/image_files"
path="/data_disk/home/sejung/Patch-NetVLAD/patchnetvlad/mobius/union"
file_list=os.listdir(path)

for i in file_list:
    print(i)
    # f = open("patchnetvlad/dataset_imagenames/image_names_index.txt", 'a')
    f = open("/data_disk/home/sejung/Patch-NetVLAD/patchnetvlad/dataset_imagenames/mobius_db.txt", 'a')
    f.write(i+'\n')

f.close()

# python feature_extract.py \
# --config_path patchnetvlad/configs/performanPce.ini \
# --dataset_file_path=image_names_query.txt \
# --dataset_root_dir=/home/sejung/Patch-NetVLAD/patchnetvlad/image_files \
# --output_features_dir patchnetvlad/output_features/first_query