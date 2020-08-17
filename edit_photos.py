import os
import cv2
import numpy as np

import argparse

def adjust_gamma(image, gamma=1.0):
   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)

#instantiate parser
parser = argparse.ArgumentParser(description="editing options")

parser.add_argument('file_dir', type=str, help='image directory')
parser.add_argument('edit_opt', type=str, help='image editing options: grayscale/ bw (black & white)/ distort / canny /')
parser.add_argument('--resize', type=int, nargs=2, help='optional argument --resize (width) (height)')

argv = parser.parse_args()

# check edit_opt argument
if (argv.edit_opt != 'grayscale') and (argv.edit_opt != 'bw') \
    and (argv.edit_opt != 'bgr') and (argv.edit_opt != 'hsv') \
    and (argv.edit_opt != 'canny') and (argv.edit_opt != 'distort') \
    and (argv.edit_opt != 'grain') and (argv.edit_opt != 'brighten') \
    and (argv.edit_opt != 'darken') and (argv.edit_opt != 'none')  :
    print('ERROR:', argv.edit_opt, 'is not a valid editing option')
    exit()

# file_dir: file directory of photos
# get list of photos in directory
try:
    img = os.listdir(argv.file_dir)
except:
    print('Error:', argv.file_dir, 'is not a valid directory')
    exit()

img.sort()

argv.file_dir.replace('/', '')
argv.file_dir.replace('\\', '')
# make directory for edited files
edi_path = os.path.join(argv.file_dir + '-' + argv.edit_opt) 
try:
    os.mkdir(edi_path)
except:
    print("Error: can't create directory named ", edi_path)
    exit()

if argv.resize is not None:
    new_width, new_height = argv.resize
    resize = True

# iterate through files and edit
for photo in img:
    if photo.lower().endswith(('.png', '.jpg', '.jpeg')):
        try:
            print("Editing:", os.path.join(argv.file_dir, photo))
            org_img = cv2.imread(os.path.join(argv.file_dir, photo))
        except:
            print("Error: can't open file", photo)
            exit()

        try:
            if argv.edit_opt == 'grayscale':
                edi_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)
            elif argv.edit_opt == 'canny':
                edi_img = cv2.Canny(org_img,100,200)
            elif argv.edit_opt == 'distort':
                edi_img = cv2.Laplacian(org_img,cv2.CV_64F)
            elif argv.edit_opt == 'grain':
                vals = len(np.unique(org_img))
                vals = .8 ** np.ceil(np.log2(vals))
                edi_img = np.random.poisson(org_img * vals) / float(vals)
            elif argv.edit_opt == 'bw':
                edi_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)
                thresh, edi_img = cv2.threshold(edi_img, 127, 255, cv2.THRESH_BINARY)
            elif argv.edit_opt == 'hsv':
                edi_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2HSV)
            elif argv.edit_opt == 'bgr':
                edi_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2RGB)
            elif argv.edit_opt == 'brighten':
                edi_img = adjust_gamma(org_img, gamma=1.8)
            elif argv.edit_opt == 'darken':
                edi_img = adjust_gamma(org_img, gamma=0.2)
     
        except:
            print("Error: can't edit file", photo)
            exit()

        if resize:
            edi_img = cv2.resize(edi_img, (new_width, new_height))

        cv2.imwrite(os.path.join(edi_path, photo), edi_img)
