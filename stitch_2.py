#!/usr/bin/env python

import os
import cv2
import imutils
from pyimagesearch.panorama_mod import Stitcher

# Set the path to images folder here
# Can modify this to a cli arg if required (using argparse) 
images_path = './images_3/'

# Function to get all files in a specified folder
def get_all_files(path):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file = os.path.join(dirpath, filename)
            files.append(file)
    return files

#Function to stitch images 2 at a time
def stitch_images(image1, image2, mode):
    print mode
    if mode == 1:
        imageA = cv2.imread(image1)
        imageA = imutils.resize(imageA, width=900)
    elif mode == 2:
        imageA = image1

    imageB = cv2.imread(image2)
    imageB = imutils.resize(imageB, width=900)

    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
    return (result, vis)

def main():
    images = get_all_files(path=images_path)
    result = images[0]

    # Hardcoding the first 2 images
    # (result, vis) = stitch_images(image1=images[0], image2=images[3], mode=1)

    # Iterating through rest of the images
    for idx, image in enumerate(images[1:]):
        print idx
        print image
        (result, vis) = stitch_images(image1=result, image2=image, mode = 1 if idx == 0 else 2)

    cv2.imwrite("./output/result.jpg", result)
    # cv2.imshow("Result", result)
    # cv2.waitKey(0)

if __name__ == '__main__':
    main()
