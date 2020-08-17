import os
import cv2
import numpy as np
import math

import argparse

parser = argparse.ArgumentParser(description="dataset file directory")

parser.add_argument('file_dir_A', type=str, help='image A directory')
parser.add_argument('file_dir_B', type=str, help='image B directory')

argv = parser.parse_args()

# file_dir: file directory of photos
# get list of photos in directory
try:
    img_A = os.listdir(argv.file_dir_B)
except:
    print('Error:', argv.file_dir_A, 'is not a valid directory')
    exit()

try:
    img_B = os.listdir(argv.file_dir_B)
except:
    print('Error:', argv.file_dir_B, 'is not a valid directory')
    exit()

argv.file_dir_A = argv.file_dir_A.replace('/', '')
argv.file_dir_A = argv.file_dir_A.replace('\\', '')
argv.file_dir_B = argv.file_dir_B.replace('/', '')
argv.file_dir_B = argv.file_dir_B.replace('\\', '')

print(argv.file_dir_A)

# make directory for edited files
file_path = os.path.join(argv.file_dir_A + '_pix2pix')
try:
    print(os.path.join(file_path, 'test'))
    os.makedirs(os.path.join(file_path, 'test'))
    os.makedirs(os.path.join(file_path, 'train'))
except:
    print("Error: can't create directory named ", file_path)
    exit()

img_A.sort()
img_B.sort()

img_count = 0
for photo in img_A:
    if photo.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_count += 1

img_split = math.ceil(img_count * (.75))


for i, photo in enumerate(img_A):
    if photo.lower().endswith(('.png', '.jpg', '.jpeg')):
        photo_A = cv2.imread(os.path.join(argv.file_dir_A, photo))
        photo_B = cv2.imread(os.path.join(argv.file_dir_B, photo))

        new_img = cv2.hconcat([photo_A, photo_B])
        
        if (i > img_split):
            cv2.imwrite(os.path.join(file_path, 'test', photo), new_img)
        else:
            cv2.imwrite(os.path.join(file_path, 'train', photo), new_img)        
        
