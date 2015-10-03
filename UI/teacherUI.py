# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher.ui'
#
# Created: Sat Oct 03 08:26:41 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(561, 431)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 250, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 250, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 250, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(71, 293, 60, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(71, 377, 60, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(71, 335, 60, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 335, 54, 12))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(80, 10, 61, 21))
        self.label_11.setMinimumSize(QtCore.QSize(54, 12))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 50, 81, 21))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 50, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.fnameButton = QtGui.QPushButton(self.centralwidget)
        self.fnameButton.setGeometry(QtCore.QRect(390, 10, 41, 23))
        self.fnameButton.setObjectName(_fromUtf8("fnameButton"))
        self.inputImgLabel = QtGui.QLabel(self.centralwidget)
        self.inputImgLabel.setGeometry(QtCore.QRect(20, 90, 150, 150))
        self.inputImgLabel.setText(_fromUtf8(""))
        self.inputImgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputImgLabel.setObjectName(_fromUtf8("inputImgLabel"))
        self.binImgLabel = QtGui.QLabel(self.centralwidget)
        self.binImgLabel.setGeometry(QtCore.QRect(190, 90, 150, 150))
        self.binImgLabel.setText(_fromUtf8(""))
        self.binImgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.binImgLabel.setObjectName(_fromUtf8("binImgLabel"))
        self.stripImgLabel = QtGui.QLabel(self.centralwidget)
        self.stripImgLabel.setGeometry(QtCore.QRect(360, 90, 150, 150))
        self.stripImgLabel.setText(_fromUtf8(""))
        self.stripImgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stripImgLabel.setObjectName(_fromUtf8("stripImgLabel"))
        self.fnameLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.fnameLineEdit.setGeometry(QtCore.QRect(150, 10, 221, 21))
        self.fnameLineEdit.setObjectName(_fromUtf8("fnameLineEdit"))
        self.colorLabel = QtGui.QLabel(self.centralwidget)
        self.colorLabel.setGeometry(QtCore.QRect(137, 293, 54, 16))
        self.colorLabel.setText(_fromUtf8(""))
        self.colorLabel.setObjectName(_fromUtf8("colorLabel"))
        self.geoLabel = QtGui.QLabel(self.centralwidget)
        self.geoLabel.setGeometry(QtCore.QRect(137, 335, 54, 16))
        self.geoLabel.setText(_fromUtf8(""))
        self.geoLabel.setObjectName(_fromUtf8("geoLabel"))
        self.stripeLabel = QtGui.QLabel(self.centralwidget)
        self.stripeLabel.setGeometry(QtCore.QRect(137, 377, 54, 16))
        self.stripeLabel.setText(_fromUtf8(""))
        self.stripeLabel.setObjectName(_fromUtf8("stripeLabel"))
        self.ansLabel = QtGui.QLabel(self.centralwidget)
        self.ansLabel.setGeometry(QtCore.QRect(360, 335, 54, 12))
        self.ansLabel.setText(_fromUtf8(""))
        self.ansLabel.setObjectName(_fromUtf8("ansLabel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "读入图像", None))
        self.label_2.setText(_translate("MainWindow", "二值化图像", None))
        self.label_3.setText(_translate("MainWindow", "纹理图像", None))
        self.label_4.setText(_translate("MainWindow", "颜色参数：", None))
        self.label_5.setText(_translate("MainWindow", "纹理参数：", None))
        self.label_6.setText(_translate("MainWindow", "几何参数：", None))
        self.label_7.setText(_translate("MainWindow", "识别结果：", None))
        self.label_11.setText(_translate("MainWindow", "选择图片：", None))
        self.pushButton_2.setText(_translate("MainWindow", "开始识别", None))
        self.pushButton_3.setText(_translate("MainWindow", "退出", None))
        self.fnameButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>nn</p></body></html>", None))
        self.fnameButton.setText(_translate("MainWindow", "浏览", None))

