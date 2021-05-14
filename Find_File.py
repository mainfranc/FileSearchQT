# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Find_File.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2 import QtGui
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(601, 475)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.txtFileName = QLineEdit(self.frame_3)
        self.txtFileName.setObjectName(u"txtFileName")

        self.horizontalLayout_3.addWidget(self.txtFileName)

        self.chkFileNameReg = QCheckBox(self.frame_3)
        self.chkFileNameReg.setObjectName(u"chkFileNameReg")

        self.horizontalLayout_3.addWidget(self.chkFileNameReg)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.txtTextToFind = QLineEdit(self.frame_4)
        self.txtTextToFind.setObjectName(u"txtTextToFind")

        self.horizontalLayout_2.addWidget(self.txtTextToFind)

        self.chkTextToFindReg = QCheckBox(self.frame_4)
        self.chkTextToFindReg.setObjectName(u"chkTextToFindReg")

        self.horizontalLayout_2.addWidget(self.chkTextToFindReg)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.txtDirectory = QLineEdit(self.frame_5)
        self.txtDirectory.setObjectName(u"txtDirectory")

        self.horizontalLayout.addWidget(self.txtDirectory)

        self.btnBrowse = QPushButton(self.frame_5)
        self.btnBrowse.setObjectName(u"btnBrowse")

        self.horizontalLayout.addWidget(self.btnBrowse)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tblFiles = QTableWidget(self.frame_2)
        if (self.tblFiles.columnCount() < 3):
            self.tblFiles.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblFiles.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblFiles.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblFiles.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tblFiles.setObjectName(u"tblFiles")
        self.tblFiles.setEnabled(True)
        header = self.tblFiles.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.horizontalLayout_4.addWidget(self.tblFiles)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblStatus = QLabel(self.frame_6)
        self.lblStatus.setObjectName(u"lblStatus")

        self.horizontalLayout_5.addWidget(self.lblStatus)

        self.horizontalSpacer = QSpacerItem(426, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.btnFindFile = QPushButton(self.frame_6)
        self.btnFindFile.setObjectName(u"btnFindFile")

        self.horizontalLayout_5.addWidget(self.btnFindFile)


        self.verticalLayout.addWidget(self.frame_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 601, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Find File", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"File name", None))
        self.chkFileNameReg.setText(QCoreApplication.translate("MainWindow", u"Use Regex", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Text to find", None))
        self.chkTextToFindReg.setText(QCoreApplication.translate("MainWindow", u"Use Regex", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Directory", None))
        self.btnBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse folder", None))
        ___qtablewidgetitem = self.tblFiles.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"File name", None));
        ___qtablewidgetitem1 = self.tblFiles.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"File path", None));
        ___qtablewidgetitem2 = self.tblFiles.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Size", None));
        self.lblStatus.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.btnFindFile.setText(QCoreApplication.translate("MainWindow", u"Find", None))
    # retranslateUi

