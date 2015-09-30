# coding: utf-8

import sys
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from demoUI import Ui_mainWindow
from learn import FLearner

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.fnameButton.clicked.connect(self.selectFile)
        self.recButton.clicked.connect(self.recognize)

        self.learner = FLearner("data3.dat")

    def selectFile(self):
        fname=QFileDialog.getOpenFileName(self,"Open file dialog","/","Image files(*.jpg)")  
        self.fnameLineEdit.setText(fname)

    def recognize(self):
        fname = self.fnameLineEdit.text()
        img = cv2.imread(str(fname))
        answer = self.learner.predict(img)[0].decode('utf-8')
        self.ansLabel.setText(u"识别结果："+answer)

        vecs = self.learner.getFeatureVector(img)
        color, geo , strip= tuple(vecs)
        color = [int(x) for x in color]
        vecString = u"颜色参数: {color}\n几何参数: {geo}\n纹理参数: {strip}".format(
                color=color, geo=round(geo, 1), strip=round(strip, 1))
        self.vecLabel.setText(vecString)


def main():
    Program = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    Program.exec_()

if __name__ == '__main__':
    main()
