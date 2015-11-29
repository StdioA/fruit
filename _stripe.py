# coding: utf-8

from __future__ import division
import cv2
import numpy as np

def getCannyStripe(img):
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresholds = cv2.Canny(img, 300, 300)

    area = reduce(lambda a,b: a*b, list(img.shape))

    return len(thresholds[thresholds.nonzero()])/area*255

def main(filename):
    image = cv2.imread(filename)

    getCannyStripe(image)

if __name__ == '__main__':
    filenames = [r"F:\SC\fruits\strawberry1.jpg", r"F:\SC\fruits\apple0.jpg"]
    for fname in filenames:
        main(fname)