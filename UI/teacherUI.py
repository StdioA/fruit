# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher.ui'
#
# Created: Sat Oct 03 10:47:35 2015
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
        MainWindow.resize(561, 413)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(561, 409))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(55, 250, 81, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(215, 250, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 250, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(71, 293, 70, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(71, 377, 70, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(71, 335, 70, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 335, 70, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_1 = QtGui.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(77, 10, 61, 25))
        self.label_1.setMinimumSize(QtCore.QSize(54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label_1.setFont(font)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.exeButton = QtGui.QPushButton(self.centralwidget)
        self.exeButton.setGeometry(QtCore.QRect(140, 50, 81, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.exeButton.setFont(font)
        self.exeButton.setObjectName(_fromUtf8("exeButton"))
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(310, 50, 75, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.quitButton.setFont(font)
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.fnameButton = QtGui.QPushButton(self.centralwidget)
        self.fnameButton.setGeometry(QtCore.QRect(392, 10, 41, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.fnameButton.setFont(font)
        self.fnameButton.setObjectName(_fromUtf8("fnameButton"))
        self.inputImgLabel = QtGui.QLabel(self.centralwidget)
        self.inputImgLabel.setGeometry(QtCore.QRect(20, 90, 150, 150))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.inputImgLabel.setFont(font)
        self.inputImgLabel.setText(_fromUtf8(""))
        self.inputImgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputImgLabel.setObjectName(_fromUtf8("inputImgLabel"))
        self.binImgLabel = QtGui.QLabel(self.centralwidget)
        self.binImgLabel.setGeometry(QtCore.QRect(190, 90, 150, 150))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.binImgLabel.setFont(font)
        self.binImgLabel.setText(_fromUtf8(""))
        self.binImgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.binImgLabel.setObjectName(_fromUtf8("binImgLabel"))
        self.stripImgLabel = QtGui.QLabel(self.centralwidget)
        self.stripImgLabel.setGeometry(QtCore.QRect(360, 90, 150, 150))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.stripImgLabel.setFont(font)
        self.stripImgLabel.setText(_fromUtf8(""))
        self.stripImgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stripImgLabel.setObjectName(_fromUtf8("stripImgLabel"))
        self.fnameLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.fnameLineEdit.setGeometry(QtCore.QRect(150, 10, 221, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.fnameLineEdit.setFont(font)
        self.fnameLineEdit.setObjectName(_fromUtf8("fnameLineEdit"))
        self.colorLabel = QtGui.QLabel(self.centralwidget)
        self.colorLabel.setGeometry(QtCore.QRect(146, 293, 120, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.colorLabel.setFont(font)
        self.colorLabel.setText(_fromUtf8(""))
        self.colorLabel.setObjectName(_fromUtf8("colorLabel"))
        self.geoLabel = QtGui.QLabel(self.centralwidget)
        self.geoLabel.setGeometry(QtCore.QRect(146, 335, 120, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.geoLabel.setFont(font)
        self.geoLabel.setText(_fromUtf8(""))
        self.geoLabel.setObjectName(_fromUtf8("geoLabel"))
        self.stripLabel = QtGui.QLabel(self.centralwidget)
        self.stripLabel.setGeometry(QtCore.QRect(146, 377, 120, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.stripLabel.setFont(font)
        self.stripLabel.setText(_fromUtf8(""))
        self.stripLabel.setObjectName(_fromUtf8("stripLabel"))
        self.ansLabel = QtGui.QLabel(self.centralwidget)
        self.ansLabel.setGeometry(QtCore.QRect(369, 335, 120, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.ansLabel.setFont(font)
        self.ansLabel.setText(_fromUtf8(""))
        self.ansLabel.setObjectName(_fromUtf8("ansLabel"))
        self.colorFrame = QtGui.QFrame(self.centralwidget)
        self.colorFrame.setGeometry(QtCore.QRect(270, 289, 30, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.colorFrame.setFont(font)
        self.colorFrame.setAutoFillBackground(True)
        self.colorFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.colorFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.colorFrame.setObjectName(_fromUtf8("colorFrame"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.quitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "水果图片识别及处理", None))
        self.label.setText(_translate("MainWindow", "读入图像", None))
        self.label_2.setText(_translate("MainWindow", "二值化图像", None))
        self.label_3.setText(_translate("MainWindow", "纹理图像", None))
        self.label_4.setText(_translate("MainWindow", "颜色参数：", None))
        self.label_5.setText(_translate("MainWindow", "纹理参数：", None))
        self.label_6.setText(_translate("MainWindow", "几何参数：", None))
        self.label_7.setText(_translate("MainWindow", "识别结果：", None))
        self.label_1.setText(_translate("MainWindow", "选择图片：", None))
        self.exeButton.setText(_translate("MainWindow", "开始识别", None))
        self.quitButton.setText(_translate("MainWindow", "退出", None))
        self.fnameButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>nn</p></body></html>", None))
        self.fnameButton.setText(_translate("MainWindow", "浏览", None))

