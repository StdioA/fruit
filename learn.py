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
    strip = [x[3] for x in data]

    ndata = []

    # for n in names:
    #     print n.decode('utf-8').encode('utf-8')

    for c, g, s in zip(color, geo, strip):
            ndata.append(np.concatenate((c, [g], [s]))) 

    clf.fit(ndata, names)

    return clf

def predict():
    a = main.main(r'F:\SC\fruits\pear.jpg')
    color, geo , strip= a[1], a[2], a[3]
    return clf.predict(np.concatenate((color, [geo], [strip])))

if __name__ == '__main__':
    clf = svm.SVC(gamma=0.001, C=100.)
    # clf = cluster.KMeans()
    learn("data3.dat")
    print predict()[0].decode('utf-8').encode('gbk')
    
