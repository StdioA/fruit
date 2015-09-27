# coding: utf-8

"""
图片处理程序，返回图片特征
"""

from __future__ import division
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

import fruitRec
import getImgFeature
# from getLBP import getLBP

data = []

def process(oriImg):

    # oriImg = cv2.imread(filename)

    biImg = fruitRec.getEle(oriImg)

    color = getImgFeature.getColorFeature(oriImg, biImg)
    geo = getImgFeature.getGeoFeature(biImg)
    stripe = getImgFeature.getCannyStripe(oriImg)
    # LBP = getLBP(oriImg)

    area, length = geo
    eig = (length**2)/area

    # cv2.imshow("ori", oriImg)
    # cv2.imshow("bi", biImg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # return [filename.split("\\")[1].decode('gbk').encode('utf-8'), color.tolist(), eig, stripe]
    return [color.tolist(), eig, stripe]


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
    with file("data3.dat", "w") as datafile:
        # print data
        pickle.dump(data, datafile)

    # z = np.zeros(len(data))
    # c = np.array([x[2] for x in data])
    # plt.plot(c, z)
    # plt.show()
