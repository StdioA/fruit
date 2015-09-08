# coding: utf-8

import cPickle as pickle
from sklearn import svm

with file("data.dat", "r") as datafile:
    data = pickle.load(datafile)

color = [x[1] for x in data]
fruit = [x[0] for x in data]


clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(color, fruit)

# print clf.predict([94, 244, 89])
print clf.predict([80, 254, 215])