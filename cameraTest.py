# coding: utf-8

import cv2

import fruitRec

def test():
    device = cv2.VideoCapture(1)
    offset = 0
    def onChange(val):
        global offset
        success, img = device.read()
        offset = val
        img += offset
        biImg = fruitRec.getEle(img)
        LUVImg = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)

        cv2.imshow("Img", img)
        cv2.imshow("LUV", LUVImg)
        cv2.imshow('bi', biImg)

    while True:
        success, img = device.read()
        if success:
            # img = (lambda x: x*1.4 if x*1.4<=255 else 255)(img)
            # img *= 1.3
            img += offset

            biImg = fruitRec.getEle(img)
            LUVImg = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)

            cv2.imshow("Img", img)
            cv2.createTrackbar("", "Img", 0, 100, onChange)
            cv2.imshow("LUV", LUVImg)
            cv2.imshow('bi', biImg)
            key = cv2.waitKey(1)
            if key == 27:
                break
    cv2.destroyAllWindows()
    device.release()

if __name__ == '__main__':
    test()
