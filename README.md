# imageCompare
python + opencv = script to compare 2 images

**usage:** *image_compare.py [-h] -a IMGA -b IMGB [-v] [-s]*    
**optional arguments:**   
-h, --help            show this help message and exit   
-a IMGA, --imgA IMGA  first image   
-b IMGB, --imgB IMGB  second image    
-v, --verbose         display windows with intermediate images    
-s, --store           save the comparison results

# outputs    
A score from 1.0 (equal images) to 0.0 (totally different images).

# thanks   
This code is an adaptation from this source:    
http://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/
