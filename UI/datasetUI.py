# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataset.ui'
#
# Created: Sat Oct 03 11:11:43 2015
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
        MainWindow.resize(481, 246)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 80, 391, 30))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.datasetLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.datasetLineEdit.setObjectName(_fromUtf8("datasetLineEdit"))
        self.horizontalLayout_2.addWidget(self.datasetLineEdit)
        self.datasetButton = QtGui.QPushButton(self.layoutWidget)
        self.datasetButton.setObjectName(_fromUtf8("datasetButton"))
        self.horizontalLayout_2.addWidget(self.datasetButton)
        self.exeButton = QtGui.QPushButton(self.centralwidget)
        self.exeButton.setGeometry(QtCore.QRect(174, 170, 141, 51))
        self.exeButton.setObjectName(_fromUtf8("exeButton"))
        self.statusLabel = QtGui.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(53, 130, 381, 31))
        self.statusLabel.setText(_fromUtf8(""))
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 30, 391, 30))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.dataDirLineEdit = QtGui.QLineEdit(self.widget)
        self.dataDirLineEdit.setObjectName(_fromUtf8("dataDirLineEdit"))
        self.horizontalLayout.addWidget(self.dataDirLineEdit)
        self.dataDirButton = QtGui.QPushButton(self.widget)
        self.dataDirButton.setObjectName(_fromUtf8("dataDirButton"))
        self.horizontalLayout.addWidget(self.dataDirButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "数据集生成器", None))
        self.label_2.setText(_translate("MainWindow", "数据集存放目录：", None))
        self.datasetButton.setText(_translate("MainWindow", "浏览", None))
        self.exeButton.setText(_translate("MainWindow", "生成数据集", None))
        self.label.setText(_translate("MainWindow", "数据文件夹：", None))
        self.dataDirButton.setText(_translate("MainWindow", "浏览", None))

