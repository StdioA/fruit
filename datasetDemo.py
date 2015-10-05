# coding: utf-8

import os
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from UI.datasetUI import Ui_MainWindow
from core.datasetMaker import makeDataset

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)

        self.setupUi(self)

        self.dataDirButton.clicked.connect(self.selectDataDir)
        self.datasetButton.clicked.connect(self.selectDatasetDir)
        self.exeButton.clicked.connect(self.makeDataset)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def selectDataDir(self):
        fname = QFileDialog.getExistingDirectory(self,"Open Data Directory","./")  
        self.dataDirLineEdit.setText(fname)

    def selectDatasetDir(self):
        fname = QFileDialog.getExistingDirectory(self,"Select Dataset Directory","./")  
        self.datasetLineEdit.setText(fname)

    def makeDataset(self):
        picDirName = str(self.dataDirLineEdit.text())
        dsFname = str(self.datasetLineEdit.text())
        dsFname = os.path.join(dsFname, 'data.dat')

        # thread = QThread
        # self.statusLabel.setText(u"正在生成数据集，程序可能无响应，请稍等")
        # self.statusLabel.show()
        # __import__("time").sleep(3)
        # QThread.sleep(3)
        makeDataset(picDirName, dsFname)
        self.statusLabel.setText(u"成功生成数据集！")


def main():
    Program = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    Program.exec_()

if __name__ == '__main__':
    main()

