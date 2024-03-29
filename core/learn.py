# coding: utf-8

"""
机器学习程序
"""

import cPickle as pickle
from sklearn import svm
import numpy as np
import cv2

import picProcess


class FLearner(object):
    """\
    The fruit recognizer
    """

    def __init__(self, dataset):
        self.clf = svm.SVC(kernel='poly', degree=3,gamma=0.001, C=100.)

        with file(dataset, "r") as datafile:
            data = pickle.load(datafile)

        names = [x[0] for x in data]
        color = [x[1] for x in data]
        geo = [x[2] for x in data]
        strip = [x[3] for x in data]

        ndata = []

        for c, g, s in zip(color, geo, strip):
                ndata.append(np.concatenate((c, [g], [s]))) 
        self.clf.fit(ndata, names)

    def getFeatureVector(self, img):
        return tuple(picProcess.process(img))

    def predict(self, img, debug=False):
        data = picProcess.process(img)
        color, geo , strip= tuple(data)

        # debug模式返回特征向量
        if debug:
            return self.clf.predict(np.concatenate((color, [geo], [strip])))[0], color, geo, strip
        else:
            return self.clf.predict(np.concatenate((color, [geo], [strip])))[0]

if __name__ == '__main__':
    
    learner = FLearner("data3.dat")

    fname = r'F:\apple.jpg'
    img = cv2.imread(fname)

    # print learner.predict(img).decode('utf-8')#.encode('gb18030')
    print learner.predict(img)
    
