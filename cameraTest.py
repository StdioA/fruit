# coding: utf-8

import cv2
import numpy as np

import fruitRec

class Camera(object):
    def __init__(self):
        self.bright = 0
        self.contrast = 10

    def __onBrightChange(self, value):
        self.bright = value

    def __onContrastChange(self, value):
        self.contrast = value

    def __pixelProcess(self, pix):
        pix = pix*self.contrast + self.bright
        if pix > 255:
            pix = 255
        return pix

    def test(self):
        device = cv2.VideoCapture(1)
        offset = 0

        #     cv2.imshow("Img", img)
        #     cv2.imshow("LUV", LUVImg)
        #     cv2.imshow('bi', biImg)

        while True:
            success, img = device.read()
            if success:
                # 图像亮度&对比度调整
                img = np.array(img, int)                                            # 转为int防止溢出
                img = img*self.contrast/10 + self.bright                
                val = (img<=255)
                mask = np.ones_like(img)*255
                img = img*val + mask*~val
                img = np.array(img, np.uint8)
                # print img

                biImg = fruitRec.getEle(img)
                LUVImg = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)

                cv2.imshow("Img", img)
                cv2.createTrackbar("Bright", "Img", self.bright, 100, self.__onBrightChange)
                cv2.createTrackbar("Contrast", "Img", self.contrast, 30, self.__onContrastChange)
                cv2.imshow("LUV", LUVImg)
                cv2.imshow('bi', biImg)
                key = cv2.waitKey(1)
                if key == 27:
                    break
        cv2.destroyAllWindows()
        device.release()

if __name__ == '__main__':
    camera = Camera()
    camera.test()
