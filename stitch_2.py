#!/usr/bin/env python

import os
import cv2
import imutils
from incl.panorama_mod import Stitcher

# Set the path to images folder here
# Can modify this to a cli arg if required (using argparse) 
images_path = 'C:\\Users\\Nikhil\\Desktop\\panorama-stitching\\panorama-stitching\\images\\Images'

# Function to get all files in a specified folder
def getAllFiles(path):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file = os.path.join(dirpath, filename)
            files.append(file)
    return files

#Function to stitch images 2 at a time
def stitchImages(image1, image2, mode):
    print mode
    if mode == 1:
        imageA = readFromDiskAndResize(image1)
        imageB = readFromDiskAndResize(image2)
    elif mode == 2:
        imageA = readFromDiskAndResize(image1)
        imageB = image2

    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
    return (result, vis)

def readFromDiskAndResize(location):
    image = cv2.imread(location)
    image = imutils.resize(image, width=500)
    return image

def main():
    images = getAllFiles(path=images_path)
    result = images[0]

    # Iterating through rest of the images
    for idx, image in enumerate(images[1:]):
        (result, vis) = stitchImages(image1=image, image2=result, mode = 1 if idx == 0 else 2)
        #cv2.imwrite("C:\\Users\\Nikhil\\Desktop\\Mtech-Thesis-master\\Mtech-Thesis-master-with-FLANN\\output\\result"+ str(idx) +".png", result)

    cv2.imwrite("C:\\Users\\Nikhil\\Desktop\\Mtech-Thesis-master\\Mtech-Thesis-master-with-FLANN\\output\\result.png", result)

if __name__ == '__main__':
    main()
