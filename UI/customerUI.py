# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\customer.ui'
#
# Created: Mon Oct 05 11:16:35 2015
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
        MainWindow.resize(709, 435)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(80, 60))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(120, 60))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setContentsMargins(10, -1, 20, -1)
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.weightLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.weightLabel.setFont(font)
        self.weightLabel.setObjectName(_fromUtf8("weightLabel"))
        self.gridLayout_3.addWidget(self.weightLabel, 3, 0, 1, 1)
        self.valueLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.valueLabel.setFont(font)
        self.valueLabel.setObjectName(_fromUtf8("valueLabel"))
        self.gridLayout_3.addWidget(self.valueLabel, 2, 0, 1, 1)
        self.valueEdit = QtGui.QLineEdit(self.centralwidget)
        self.valueEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.valueEdit.setFont(font)
        self.valueEdit.setObjectName(_fromUtf8("valueEdit"))
        self.gridLayout_3.addWidget(self.valueEdit, 2, 1, 1, 1)
        self.fruitLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.fruitLabel.setFont(font)
        self.fruitLabel.setObjectName(_fromUtf8("fruitLabel"))
        self.gridLayout_3.addWidget(self.fruitLabel, 1, 0, 1, 1)
        self.weightEdit = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.weightEdit.setFont(font)
        self.weightEdit.setObjectName(_fromUtf8("weightEdit"))
        self.gridLayout_3.addWidget(self.weightEdit, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(0, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 5, 1, 1, 1)
        self.totalLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.totalLabel.setFont(font)
        self.totalLabel.setObjectName(_fromUtf8("totalLabel"))
        self.gridLayout_3.addWidget(self.totalLabel, 4, 0, 1, 1)
        self.totalEdit = QtGui.QLineEdit(self.centralwidget)
        self.totalEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.totalEdit.setFont(font)
        self.totalEdit.setObjectName(_fromUtf8("totalEdit"))
        self.gridLayout_3.addWidget(self.totalEdit, 4, 1, 1, 1)
        self.confirmButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.confirmButton.setFont(font)
        self.confirmButton.setObjectName(_fromUtf8("confirmButton"))
        self.gridLayout_3.addWidget(self.confirmButton, 3, 2, 1, 1)
        self.fruitBox = QtGui.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.fruitBox.setFont(font)
        self.fruitBox.setEditable(False)
        self.fruitBox.setObjectName(_fromUtf8("fruitBox"))
        self.gridLayout_3.addWidget(self.fruitBox, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(0, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.photoLabel = QtGui.QLabel(self.centralwidget)
        self.photoLabel.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.photoLabel.sizePolicy().hasHeightForWidth())
        self.photoLabel.setSizePolicy(sizePolicy)
        self.photoLabel.setMinimumSize(QtCore.QSize(3, 4))
        self.photoLabel.setSizeIncrement(QtCore.QSize(3, 4))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.photoLabel.setFont(font)
        self.photoLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.photoLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.photoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.photoLabel.setObjectName(_fromUtf8("photoLabel"))
        self.gridLayout.addWidget(self.photoLabel, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.weightEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.confirmButton.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "水果识别计价软件", None))
        self.weightLabel.setText(_translate("MainWindow", "重量：", None))
        self.valueLabel.setText(_translate("MainWindow", "单价：", None))
        self.fruitLabel.setText(_translate("MainWindow", "结果：", None))
        self.totalLabel.setText(_translate("MainWindow", "总价：", None))
        self.confirmButton.setText(_translate("MainWindow", "确定", None))
        self.photoLabel.setText(_translate("MainWindow", "摄像头采集到的图像", None))

