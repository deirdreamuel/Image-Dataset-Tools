# Image Dataset Tools
Python program that utilizes OpenCV and Numpy for editing images and creating datasets for machine learning models such as Pix2Pix and CycleGan. There are multiple options and various effects to apply to a directory of images.

## Installation
```
git clone https://github.com/xerzen/Image-Dataset-Tools.git
```
or just download as zip.

### Python: download [here](https://www.python.org/downloads/)

### install numpy
using pip: 
```
pip install numpy
```

### install opencv
using pip: 
```
pip install opencv-python
```


## Usage sample

### edit_dataset.py
```
python edit_dataset.py /directoryA /directoryB --split (test/train ratio) --pix2pix --cyclegan
```
### edit_photos.py
``` 
python edit_photos.py /directory bw --resize (width) (height)
```

## Documentation

### edit_dataset.py
```
python edit_dataset.py file_dir_A file_dir_B --split float(split  ratio) --pix2pix --cyclegan
```

```file_dir_A``` : directory of images for input.

```file_dir_B``` : directory of images for output.

``` --split float(split ratio) ``` (optional): ratio to split images for testing vs training.

```--pix2pix``` (optional): prepare dataset for pix2pix machine learning model.

```--cyclegan``` (optional): prepare dataset for cyclegan machine learning model.


### edit_photos.py
```
python edit_photos.py file_dir edit_opt --resize (height) (width)
```
```file_dir``` : directory of images to edit

```edit_opt``` : editing option for images, (grayscale, bw, bgr, hsv, canny, distort, grain, brighten, darken, none)

```--resize (height) (width)``` (optional): resizes images to specified height and width