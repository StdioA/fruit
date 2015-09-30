# coding: utf-8

import cv2
import numpy as np
import os

import cv

def OtsuGray( grayImage ,debug = 0):
    # 如果图片是Mat对象，则转换为Image对象
    if type(grayImage) == cv.cvmat:
        grayImage = cv.GetImage(grayImage)
    elif isinstance(grayImage, np.ndarray):
    	grayImage = cv.GetImage(cv.fromarray(grayImage))
        
    # 创建Hist
    hist = cv.CreateHist([256],cv.CV_HIST_ARRAY,[[0,256]])
    cv.ClearHist(hist)
    # 计算Hist
    cv.CalcHist([grayImage],hist)

    # 开始计算
    # 计算总亮度
    totalH = 0
    for h in range(0,256):
        v = cv.QueryHistValue_1D(hist,h)
        if v == 0 : continue
        totalH += v*h
        if debug > 3 : print "t=%d,%d,%d"%(h,totalH,v*h)
        

    width  = grayImage.width
    height = grayImage.height
    total  = width*height
    
    if debug > 1 : print "总像素:%d;总亮度:%d平均亮度:%0.2f"%(total,totalH,totalH/total)

    # t=0和t=255的时候无法构成分割，所以从t=1开始计算一致到t=255
    # 初始化v值
    v = 0

    gMax = 0.0
    tIndex = 0
    
    # temp
    n0Acc = 0
    n1Acc = 0
    n0H   = 0
    n1H   = 0
    for t in range(1,255):
        v = cv.QueryHistValue_1D(hist,t-1)
        if v == 0: continue
        
        n0Acc += v          #灰度小于t的像素的数目
        n1Acc = total - n0Acc #灰度大于等于t的像素的数目
        n0H += (t-1)*v          #灰度小于t的像素的总亮度
        n1H = totalH - n0H  #灰度大于等于t的像素的总亮度

        if n0Acc > 0 and n1Acc > 0:
            u0 = n0H/n0Acc # 灰阶小于t的平均灰度
            u1 = n1H/n1Acc # 灰阶大于等于t的平均灰度
            w0 = n0Acc/total # 灰阶小于t的像素比例
            w1 = 1.0-w0      # 灰阶大于等于t的像素的比例
            uD = u0-u1
            g = w0 * w1 * uD * uD

            if debug > 2: print "t=%3d; u0=%.2f,u1=%.2f,%.2f;n0H=%d,n1H=%d; g=%.2f"\
               %(t,u0,u1,u0*w0+u1*w1,n0H,n1H,g)

            if gMax < g:
                gMax   = g
                tIndex = t
        
    if debug >0 : print "gMaxValue=%.2f; t = %d ; t_inv = %d"\
               %(gMax,tIndex,255-tIndex)            

    return tIndex


def getEle(img, otsu=False):
	u'''二值化处理'''
	LUVImg = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)

	blurImg = cv2.medianBlur(LUVImg, 5)
	grayImg = cv2.cvtColor(blurImg, cv2.COLOR_BGR2GRAY)

	if otsu:
		threshold = OtsuGray(grayImg)-8
	else:
		threshold = 127

	biImg = cv2.threshold(grayImg, threshold, 255, cv2.THRESH_BINARY_INV)[1]
	# biImg = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,25,2)
	# biImg = adaptiveThreshold(grayImg,255,ADAPTIVE_THRESH_MEAN_C,THRESH_BINARY,5,2)
	return biImg

def main(filename):

	OriImg = cv2.imread(filename)

	final = getEle(OriImg)
	
	cv2.imshow(filename, final)
	cv2.imshow(filename+'otsu', getEle(OriImg, True))
	key = cv2.waitKey(0)
	if key == 27:
		raise KeyboardInterrupt
	cv2.destroyWindow(filename)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	# main('F:/banana.jpg')
	for root, dirs, files in os.walk("../pictures"):
		if files:
			for fname in files:               
				main(os.path.sep.join([root, fname]))
