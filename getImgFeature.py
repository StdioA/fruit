# coding: utf-8

from __future__ import division
import numpy as np
import cv2
# from getElem import getEle

def getGeoFeature(img, showResult=None):
    """\
    getGeoFeature(img) -> area, length
        Return the area and circumference of an binary image.
        Parameters:
            img: an binary image represented as an numpy 2D-array, whose valid element is an non-zero number
        Return values:
            area: The area of the valid part of binary image
            length: the circumference of the valid part of binary image
    """

    height, width = tuple(img.shape)
    mask = np.matrix([[0,   0,  0],
                      [0,   255,0],
                      [0,   0,  0]])
    isIsolated = lambda img, i, j: (img[i-1:i+2, j-1:j+2] == mask)#.all()        # 判断图像上的某个点是否为孤立点

    def isIsolated(img, i, j):
        iso = (img[i-1:i+2, j-1:j+2] == mask)
        if isinstance(iso, bool):
            return iso
        else:
            return iso.all()

    getArea = lambda img: len(img[img.nonzero()])                               # 统计二值化图像中非零点的个数

    area = getArea(img)                                                         # 图像非零点的个数即为图像的面积

    # 绘制二值图的边缘
    # contour = np.zeros(img.shape, np.uint8)
    # for i in range(height):
    #     for j in range(width):                                                  # 从左到右判断第一个扫描到的点
    #         if img[i][j] and not isIsolated(img, i, j):
    #             contour[i][j] = 255
    #             break
    #     for j in reversed(range(width)):                                        # 从右往左
    #         if img[i][j] and not isIsolated(img, i, j):
    #             contour[i][j] = 255
    #             break

    # for j in range(width):
    #     for i in range(height):                                                 # 从上往下
    #         if img[i][j] and not isIsolated(img, i, j):
    #             contour[i][j] = 255
    #             break
    #     for i in reversed(range(height)):                                       # 从下往上
    #         if img[i][j] and not isIsolated(img, i, j):
    #             contour[i][j] = 255
    #             break

    # length = getArea(contour)                                                   # 边缘图像的非零点个数即为周长

    # length = max([len(x) for x in cv2.Canny(img, 127, 200)])

    contours = cv2.Canny(img, 127, 200)
    lens = sorted([len(x) for x in contours], reverse=True)

    length = lens[0]+lens[1]


    if showResult:
        # 显示/保存边缘图像
        cv2.imwrite('contour.jpg', contour)
        # cv2.imshow('Image of Contour', contour)
        # key = cv2.waitKey(0)
        # if key == 27:
        #     raise Exception('退出')
        # cv2.destroyAllWindows()

    return area, length

def getColorFeature(img, bin, showAve=None):
    """\
    getColorFeature(img) -> color
        Return the average color of the image.
        Parameters:
            img: the original image.
            bin: an binary image related to the original image,
                 represented as an numpy 2D-array, whose valid element is an non-zero number
        Return values:
            color: a numpy array made of [B, R, G], which means the average color of the image. 
    """

    # area = len(bin[bin.nonzero()])
    area = 0
    height, width = tuple(bin.shape)

    colorSum = np.array([0,0,0])
    for x in xrange(height):
        for y in xrange(width):
            if not bin[x, y]:
                colorSum += img[x, y]
                area += 1
    # for x, y in np.transpose(bin.nonzero()):
    #     colorSum += img[x, y]

    aveColor = colorSum/area

    if showAve:
        aveImg = cv2.resize(img, (100, 100))
        for i in range(100):
            for j in range(100):
                aveImg[i, j] = aveColor
        cv2.imshow('Origin', img)
        cv2.imshow('aveColor', aveImg)                                            # 显示平均色, 将平均色表示为100*100的色块
        cv2.imshow('bin', bin)
        key = cv2.waitKey(0)
        if key == 27:
            raise Exception('退出')
        cv2.destroyAllWindows()

    return aveColor

def main(filename, oriname):
    ori = cv2.imread(oriname, cv2.IMREAD_COLOR)
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    bin = getEle(img)

    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # bin = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)[1]               # 二值图

    area, length = getGeoFeature(bin)
    color = getColorFeature(ori, bin)

    print 'Area:', area                                                           # 二值图面积
    print 'Length of countour:', length                                           # 二值图周长
    print 'Geometry eigenvalue:', (length**2)/area                                # 水果的形状参数
    print 'Average color:\n\
           \tR: %.1f, G: %.1f, B: %.1f'\
           % (color[2], color[1], color[0])                                       # 水果的平均色

def getCannyStripe(img):
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresholds = cv2.Canny(img, 300, 300)

    area = reduce(lambda a,b: a*b, list(img.shape))

    return len(thresholds[thresholds.nonzero()])/area*25500

    
if __name__ == '__main__':
    fs = ['orange/bin.jpg', 'apple/bin.jpg', 'banana/bin.jpg']
    oris = ['orange/orange.jpg', 'apple/apple.jpg', 'banana/banana.jpg']
    for index, fname in enumerate(fs):
        main(fname, oris[index])
