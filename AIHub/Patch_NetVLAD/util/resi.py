import cv2
import os
from PIL import Image
import pandas as pd
import numpy as np
import re
import glob
import multiprocessing
import time


# file_list = os.listdir("/data_disk/space_search/netvlad_training/10m_london_bing")

# for i in file_list:
# 	try:
# 		#print(file_list[i])
# 		img = cv2.imread("/data_disk/space_search/netvlad_training/10m_london_bing/"+ i)
# 		#print(img.shape)
# 		crop_img = img[0:600, 300:1400]
# 		resize_img = cv2.resize(crop_img, (256, 256), interpolation=cv2.INTER_AREA)
# 		#print(cv2.mean(crop_img))
# 		if (cv2.mean(resize_img)[0] and cv2.mean(resize_img)[1] and cv2.mean(resize_img)[2]) < 180.0:
# 			cv2.imwrite(i, resize_img)
# 		else:
# 			print(i,": ",cv2.mean(resize_img))
# 	except Exception as e:
# 		print(str(e))

def img_cropping_resize(image):
	file_list = os.listdir(image)
	for i in file_list:
		try:
			#print(image)
			img =cv2.imread('/data_disk/space_search/netvlad_training/gapyeong_2/'+i)
			crop_img = img[0:600, 300:1400]
			resize_img = cv2.resize(crop_img, (256, 256), interpolation=cv2.INTER_AREA)
			# print(img)
			# print(resize_img)
			# if (cv2.mean(resize_img)[0] and cv2.mean(resize_img)[1] and cv2.mean(resize_img)[2]) < 180.0:
			cv2.imwrite('/data_disk/space_search/netvlad_training/gap/'+i, resize_img)
			# else:
			# 	print(resize_img,": ",cv2.mean(resize_img))
		except Exception as e:
			print(str(e))


if __name__ =='__main__':
    # images_meta=glob.glob(img_path)
    
    imgfile_list = glob.glob(f'/data_disk/space_search/netvlad_training/gapyeong_2/')

    try:
        pool=multiprocessing.Pool(processes=65)
        pool.map(img_cropping_resize, imgfile_list)
    
    except:
        pass

# 출력
# img.shape = (360, 480, 3)
# resize_img.shape = (300, 300, 3)
