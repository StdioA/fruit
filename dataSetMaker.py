# coding: utf-8

"""
数据集生成程序
"""

import multiprocessing
import pickle
import picProcess

def main(picDirName, dsFname):
    fnames = []
    for root, dirs, files in os.walk(picDirName):
        if files:
            for fname in files:               
                # main(os.path.sep.join([root, fname]))
                fnames.append(os.path.sep.join([root, fname]))

    pool = multiprocessing.Pool(4)
    data = pool.map(picProcess.process, fnames)
    pool.close()
    pool.join()

    print len(data)
    with file(dsFname, "w") as datafile:
        # print data
        pickle.dump(data, datafile)

if __name__ == '__main__':
    main("../pictures", "data3.dat")
