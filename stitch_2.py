#!/usr/bin/env python

import os
import cv2
import imutils
from pyimagesearch.panorama import Stitcher

# Set the path to images folder here
# Can modify this to a cli arg if required (using argparse) 
images_path = './images/'

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
    if mode == 1:
        imageA = cv2.imread(image1)
    elif mode == 2:
        imageA = image1

    imageA = imutils.resize(imageA, width=400)
    imageB = cv2.imread(image2)
    imageB = imutils.resize(imageB, width=400)
    cv2.imshow("A", imageA)
    cv2.imshow("B", imageB)

    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
    return (result, vis)

def main():
    images = get_all_files(path=images_path)

    # Hardcoding the first 2 images
    (result, vis) = stitch_images(image1=images[0], image2=images[1], mode=1)

    # Iterating through rest of the images
    for image in images[2:]:
        if result is None:
            os.sys.exit("Images can't be stitched");
        (result, vis) = stitch_images(image1=result, image2=image, mode=2)

    cv2.imshow("Result", result)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
