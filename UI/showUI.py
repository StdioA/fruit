# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show.ui'
#
# Created: Sun Oct 04 09:49:29 2015
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
        MainWindow.resize(449, 370)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setMargin(12)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_1 = QtGui.QLabel(self.centralwidget)
        self.label_1.setMinimumSize(QtCore.QSize(54, 12))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label_1.setFont(font)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.horizontalLayout_4.addWidget(self.label_1)
        self.fnameLineEdit = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.fnameLineEdit.setFont(font)
        self.fnameLineEdit.setObjectName(_fromUtf8("fnameLineEdit"))
        self.horizontalLayout_4.addWidget(self.fnameLineEdit)
        self.fnameButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.fnameButton.setFont(font)
        self.fnameButton.setObjectName(_fromUtf8("fnameButton"))
        self.horizontalLayout_4.addWidget(self.fnameButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.exeButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exeButton.sizePolicy().hasHeightForWidth())
        self.exeButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.exeButton.setFont(font)
        self.exeButton.setObjectName(_fromUtf8("exeButton"))
        self.horizontalLayout.addWidget(self.exeButton)
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quitButton.sizePolicy().hasHeightForWidth())
        self.quitButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.quitButton.setFont(font)
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.horizontalLayout.addWidget(self.quitButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.inputImgLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.inputImgLabel.setFont(font)
        self.inputImgLabel.setAutoFillBackground(True)
        self.inputImgLabel.setText(_fromUtf8(""))
        self.inputImgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputImgLabel.setObjectName(_fromUtf8("inputImgLabel"))
        self.horizontalLayout_2.addWidget(self.inputImgLabel)
        self.binImgLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.binImgLabel.setFont(font)
        self.binImgLabel.setAutoFillBackground(True)
        self.binImgLabel.setText(_fromUtf8(""))
        self.binImgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.binImgLabel.setObjectName(_fromUtf8("binImgLabel"))
        self.horizontalLayout_2.addWidget(self.binImgLabel)
        self.stripImgLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.stripImgLabel.setFont(font)
        self.stripImgLabel.setAutoFillBackground(True)
        self.stripImgLabel.setText(_fromUtf8(""))
        self.stripImgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stripImgLabel.setObjectName(_fromUtf8("stripImgLabel"))
        self.horizontalLayout_2.addWidget(self.stripImgLabel)
        spacerItem2 = QtGui.QSpacerItem(0, 48, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.colorLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.colorLabel.setFont(font)
        self.colorLabel.setText(_fromUtf8(""))
        self.colorLabel.setObjectName(_fromUtf8("colorLabel"))
        self.gridLayout.addWidget(self.colorLabel, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.stripLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.stripLabel.setFont(font)
        self.stripLabel.setText(_fromUtf8(""))
        self.stripLabel.setObjectName(_fromUtf8("stripLabel"))
        self.gridLayout.addWidget(self.stripLabel, 2, 1, 1, 1)
        self.geoLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.geoLabel.setFont(font)
        self.geoLabel.setText(_fromUtf8(""))
        self.geoLabel.setObjectName(_fromUtf8("geoLabel"))
        self.gridLayout.addWidget(self.geoLabel, 1, 1, 1, 1)
        self.colorFrame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorFrame.sizePolicy().hasHeightForWidth())
        self.colorFrame.setSizePolicy(sizePolicy)
        self.colorFrame.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.colorFrame.setFont(font)
        self.colorFrame.setAutoFillBackground(True)
        self.colorFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.colorFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.colorFrame.setObjectName(_fromUtf8("colorFrame"))
        self.gridLayout.addWidget(self.colorFrame, 0, 2, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        self.ansLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("YaHei Consolas Hybrid"))
        font.setPointSize(11)
        self.ansLabel.setFont(font)
        self.ansLabel.setText(_fromUtf8(""))
        self.ansLabel.setObjectName(_fromUtf8("ansLabel"))
        self.horizontalLayout_6.addWidget(self.ansLabel)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.quitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "图像处理及识别", None))
        self.label_1.setText(_translate("MainWindow", "选择图片：", None))
        self.fnameButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>nn</p></body></html>", None))
        self.fnameButton.setText(_translate("MainWindow", "浏览", None))
        self.exeButton.setText(_translate("MainWindow", "开始识别", None))
        self.quitButton.setText(_translate("MainWindow", "退出", None))
        self.label.setText(_translate("MainWindow", "读入图像", None))
        self.label_2.setText(_translate("MainWindow", "二值化图像", None))
        self.label_3.setText(_translate("MainWindow", "纹理图像", None))
        self.label_5.setText(_translate("MainWindow", "纹理参数：", None))
        self.label_6.setText(_translate("MainWindow", "几何参数：", None))
        self.label_4.setText(_translate("MainWindow", "颜色参数：", None))
        self.label_7.setText(_translate("MainWindow", "识别结果：", None))
