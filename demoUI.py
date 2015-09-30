# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created: Wed Sep 30 15:50:35 2015
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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(435, 205)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        mainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.fnameLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.fnameLineEdit.setGeometry(QtCore.QRect(20, 40, 281, 21))
        self.fnameLineEdit.setObjectName(_fromUtf8("fnameLineEdit"))
        self.fnameButton = QtGui.QPushButton(self.centralwidget)
        self.fnameButton.setGeometry(QtCore.QRect(310, 40, 75, 23))
        self.fnameButton.setObjectName(_fromUtf8("fnameButton"))
        self.recButton = QtGui.QPushButton(self.centralwidget)
        self.recButton.setGeometry(QtCore.QRect(290, 80, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recButton.setFont(font)
        self.recButton.setObjectName(_fromUtf8("recButton"))
        self.vecLabel = QtGui.QLabel(self.centralwidget)
        self.vecLabel.setGeometry(QtCore.QRect(30, 80, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.vecLabel.setFont(font)
        self.vecLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.vecLabel.setObjectName(_fromUtf8("vecLabel"))
        self.ansLabel = QtGui.QLabel(self.centralwidget)
        self.ansLabel.setGeometry(QtCore.QRect(30, 130, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ansLabel.setFont(font)
        self.ansLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ansLabel.setObjectName(_fromUtf8("ansLabel"))
        self.exitButton = QtGui.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(290, 130, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.colorFrame = QtGui.QFrame(self.centralwidget)
        self.colorFrame.setGeometry(QtCore.QRect(220, 84, 21, 21))
        self.colorFrame.setAutoFillBackground(True)
        self.colorFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.colorFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.colorFrame.setObjectName(_fromUtf8("colorFrame"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), mainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Demo", None))
        self.fnameButton.setText(_translate("mainWindow", "浏览", None))
        self.recButton.setText(_translate("mainWindow", "识别", None))
        self.vecLabel.setText(_translate("mainWindow", "颜色参数: \n"
"几何参数: \n"
"纹理参数: ", None))
        self.ansLabel.setText(_translate("mainWindow", "识别结果：", None))
        self.exitButton.setText(_translate("mainWindow", "退出", None))

