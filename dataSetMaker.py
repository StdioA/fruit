# coding: utf-8

"""
数据集生成程序
"""

import multiprocessing
import pickle
import cv2
import picProcess

def getData(fname):
    img = cv2.imread(fname)
    data = picProcess.process(img)
    return [filename.split("\\")[1].decode('gbk').encode('utf-8')]+data

def main(picDirName, dsFname):
    fnames = []
    for root, dirs, files in os.walk(picDirName):
        if files:
            for fname in files:               
                # main(os.path.sep.join([root, fname]))
                fnames.append(os.path.sep.join([root, fname]))

    pool = multiprocessing.Pool(4)
    data = pool.map(getData, fnames)
    pool.close()
    pool.join()

    print len(data)
    with file(dsFname, "w") as datafile:
        # print data
        pickle.dump(data, datafile)

if __name__ == '__main__':
    main("../pictures", "data3.dat")
