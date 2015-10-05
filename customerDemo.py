# coding: utf-8

import sys
import os
import ConfigParser
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from UI.customerUI import Ui_MainWindow
from core.learn import FLearner

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)

        self.setupUi(self)

        # 读入数据集路径，建立学习模型
        config=ConfigParser.ConfigParser()
        config.read("./settings.ini")
        self.datasetPath = config.get("dataset", "path")
        self.learner = FLearner(self.datasetPath)

        # 读取水果种类及价格
        self.fruits = config.options('fruits')
        ufruits = [unicode(f, encoding='utf-8') for f in self.fruits]
        self.values = dict(config.items('fruits'))

        # 设置水果种类列表
        self.fruitBox.addItems(ufruits)
        self.fruitBox.connect(self.fruitBox,
                            SIGNAL("activated(QString)"),
                            self.selectFruit)

        # 设置重量列表
        self.weightEdit.returnPressed.connect(self.calTotalValue)
        self.confirmButton.clicked.connect(self.calTotalValue)

        # 建立temp文件夹
        if not os.path.exists('./temp'):
            os.mkdir('./temp')
        
        # 打开摄像头
        self.device = cv2.VideoCapture(1)
        if not self.device.isOpened():
            self.device = cv2.VideoCapture(0)
        if not self.device.isOpened():
            QMessageBox.critical(self,"Critical", self.tr("找不到摄像头！"))

        # 建立时钟
        self.timer = QTimer(self.photoLabel)
        self.timer.timeout.connect(self.flushImage)
        self.timer.start(0)

        self.fruitname = ""
        self.lastfruitname = ""

    def selectFruit(self, fruit):
        fruitname = str(fruit.toUtf8())
        value = self.values[fruitname]
        self.valueEdit.setText(str(value))

    def flushImage(self):
        img = self.device.read()[1]
        cv2.imwrite("./temp/image.jpg", img)

        pixmap = QPixmap()
        pixmap.load("./temp/image.jpg")
        width = self.photoLabel.width()
        self.photoLabel.setPixmap(pixmap.scaled(width, width*0.75))
        self.photoLabel.show()

        # 识别水果
        self.fruitname = self.learner.predict(img)
        if self.fruitname != self.lastfruitname:
            print self.fruitname.decode('utf-8').encode('gbk')
            self.fruitBox.setCurrentIndex(self.fruits.index(self.fruitname))
            value = self.values[self.fruitname]
            self.valueEdit.setText(str(value))

        self.lastfruitname = self.fruitname

    def calTotalValue(self):
        value = int(self.valueEdit.text())
        weight = int(self.weightEdit.text())
        total = value*weight
        self.totalEdit.setText(str(total))

def main():
    Program = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    Program.exec_()

if __name__ == '__main__':
    main()
