# coding: utf-8

import cPickle as pickle
from sklearn import svm
import numpy as np

import main

def learn(filename):
    with file(filename, "r") as datafile:
        data = pickle.load(datafile)

    names = [x[0] for x in data]
    color = [x[1] for x in data]
    geo = [x[2] for x in data]
    LBP = [x[3] for x in data]

    ndata = []

    # print np.array(LBP).shape

    for c, g, l in zip(color, geo, LBP):
        ndata.append(np.concatenate((c, [g], l.flatten())))

    clf.fit(ndata, names)

    return clf

def predict():
    # print clf.predict([94, 244, 89])
    # print clf.predict([80, 254, 215])
    a = main.main(r'F:\SC\fruits\banana.jpg')
    color, geo, LBP = a[1], a[2], a[3]

    return clf.predict(np.concatenate((color, [geo], LBP.flatten())))

if __name__ == '__main__':
    clf = svm.SVC(gamma=0.001, C=100.)
    # clf = cluster.KMeans()
    learn("data_with_LBP.dat")
    print predict()[0]
    