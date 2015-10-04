# coding: utf-8

import sys
import os
import ConfigParser
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# from UI.teacherUI import Ui_MainWindow
from UI.showUI import Ui_MainWindow
from core.learn import FLearner
from core.fruitRec import getEle

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)

        self.setupUi(self)

        self.fnameButton.clicked.connect(self.selectFile)
        self.exeButton.clicked.connect(self.execute)

        # 读入数据集路径，建立学习模型
        config=ConfigParser.ConfigParser()
        config.read("./settings.ini")
        self.datasetPath = config.get("dataset", "path")
        self.learner = FLearner(self.datasetPath)

        # 建立temp文件夹
        if not os.path.exists('./temp'):
            os.mkdir('./temp')

    def selectFile(self):
        fname = QFileDialog.getOpenFileName(self,"Open Image File","./","Image files(*.jpg)")  
        if fname:
            self.fnameLineEdit.setText(fname)

    def execute(self):
        # 打开文件
        fname = self.fnameLineEdit.text()
        img = cv2.imread(str(fname))
        if img is None:                                                             # 文件打开失败
            return

        # 显示图片
        cv2.imwrite("./temp/origin.jpg", img)
        pixmap = QPixmap()
        pixmap.load("./temp/origin.jpg")
        self.inputImgLabel.setPixmap(pixmap.scaled(self.inputImgLabel.size()))
        self.inputImgLabel.show()

        # 显示二值图
        biImg = getEle(img)
        cv2.imwrite("./temp/bin.jpg", biImg)
        pixmap = QPixmap()
        pixmap.load("./temp/bin.jpg")
        self.binImgLabel.setPixmap(pixmap.scaled(self.binImgLabel.size()))
        self.binImgLabel.show()

        # 显示纹理图像
        stripImg = cv2.Canny(img, 300, 300)
        cv2.imwrite("./temp/strip.jpg", stripImg)
        pixmap = QPixmap()
        pixmap.load("./temp/strip.jpg")
        self.stripImgLabel.setPixmap(pixmap.scaled(self.stripImgLabel.size()))
        self.stripImgLabel.show()

        # 获取特征向量及结果
        vecs = self.learner.predict(img, debug=True)
        ans, color, geo , strip = vecs
        color = [int(x) for x in color]
        self.colorLabel.setText(str(color))
        self.geoLabel.setText(str(round(geo, 1)))
        self.stripLabel.setText(str(round(strip, 1)))
        # ans = ans.decode('utf-8')
        self.ansLabel.setText(unicode(ans, 'utf-8'))

        # 显示颜色
        b, g, r = tuple(color)
        bColor=QColor(r, g, b)
        p=self.colorFrame.palette()  
        p.setColor(QPalette.Window,bColor)  
        self.colorFrame.setPalette(p)


def main():
    Program = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    Program.exec_()

if __name__ == '__main__':
    main()
