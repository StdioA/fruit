# coding: utf-8

from __future__ import division
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import multiprocessing

import fruitRec
import getImgFeature

import pickle

data = []

def main(filename):

    oriImg = cv2.imread(filename)

    biImg = fruitRec.getEle(oriImg)

    color = getImgFeature.getColorFeature(oriImg, biImg)
    geo = getImgFeature.getGeoFeature(biImg)

    area, length = geo
    eig = (length**2)/area

    # data.append([filename.split("\\")[1], color, eig])

    return [filename.split("\\")[1], color, eig]


if __name__ == '__main__':
    fnames = []
    for root, dirs, files in os.walk("../pictures"):
        if files:
            for fname in files:               
                # main(os.path.sep.join([root, fname]))
                fnames.append(os.path.sep.join([root, fname]))

    pool = multiprocessing.Pool(4)
    data = pool.map(main, fnames)
    pool.close()
    pool.join()

    print len(data)
    with file("data2.dat", "w") as datafile:
        pickle.dump(data, datafile)

    # z = np.zeros(len(data))
    # c = np.array([x[2] for x in data])
    # plt.plot(c, z)
    # plt.show()
