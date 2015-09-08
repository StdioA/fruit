# coding: utf-8

import cv2
import numpy as np
import os

def getEle(img):
	u'''二值化处理'''
	LUVImg = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)

	blurImg = cv2.medianBlur(LUVImg, 5)
	grayImg = cv2.cvtColor(blurImg, cv2.COLOR_BGR2GRAY)
	#return grayImg
	
	#动态计算阈值
	size = img.shape
	outer = grayImg[0][0]
	inner = grayImg[size[0]/2][size[1]/2]
	thre = (int(outer)+int(inner))*0.44
	# print thre

	biImg = cv2.threshold(grayImg,127,255,cv2.THRESH_BINARY_INV)[1]
	# biImg = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,25,2)
	#biImg = adaptiveThreshold(grayImg,255,ADAPTIVE_THRESH_MEAN_C,THRESH_BINARY,5,2)
	return biImg

def fillEle(img):
	u'''填充图像'''
	edges = Canny(img, 100, 200)
	# length, height = tuple(img.shape[:2])
	print img.shape
	black = np.zeros(img.shape[:2], bool)
	for edge in edges:
		print edge
		# for p in edge:
			# print p
			# black[*p] = True

	imshow("1", black)

# def main(filename):

# 	OriImg = cv2.imread(filename)
# 	k = fillEle(OriImg)

# 	final = getEle(OriImg)
# 	# imwrite('bin.jpg', final)
# 	# for t, final in enumerate(it):
# 	imshow(filename, final)
# 	key = waitKey(0)
# 	if key == 27:
# 		raise Exception
# 	# destroyWindow(filename)
# 	destroyAllWindows()

# if __name__ == '__main__':
# 	for root, dirs, files in os.walk("../pictures"):
# 		if files:
# 			for fname in files:               
# 				main(os.path.sep.join([root, fname]))
