# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/donate.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(404, 612)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelLogo = QtWidgets.QLabel(Dialog)
        self.labelLogo.setObjectName("labelLogo")
        self.horizontalLayout.addWidget(self.labelLogo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.labelDonate = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDonate.sizePolicy().hasHeightForWidth())
        self.labelDonate.setSizePolicy(sizePolicy)
        self.labelDonate.setOpenExternalLinks(True)
        self.labelDonate.setObjectName("labelDonate")
        self.verticalLayout.addWidget(self.labelDonate)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelTypeOfTheDayTitle = QtWidgets.QLabel(self.groupBox)
        self.labelTypeOfTheDayTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTypeOfTheDayTitle.setObjectName("labelTypeOfTheDayTitle")
        self.verticalLayout_3.addWidget(self.labelTypeOfTheDayTitle)
        self.labelTipOfTheDay = QtWidgets.QLabel(self.groupBox)
        self.labelTipOfTheDay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTipOfTheDay.setOpenExternalLinks(True)
        self.labelTipOfTheDay.setObjectName("labelTipOfTheDay")
        self.verticalLayout_3.addWidget(self.labelTipOfTheDay)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Donating to LibraZiK"))
        self.labelLogo.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/logo-LZK3.svg\"/></p></body></html>"))
        self.labelDonate.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Thanks for using LibraZiK !</p><p align=\"center\">You seem to be a regular user of LibraZiK.</p><p align=\"center\">Creating and maintaining this distribution<br/>is a hard and constant work that takes time.<br/><br/>That is why donations (even modest ones)<br/>are very much appreciated to help keep<br/>the motivation alive.</p><p align=\"center\">You can make a donation <a href=\"https://liberapay.com/LibraZiK/donate\"><span style=\" text-decoration: underline; color:#2980b9;\">here</span></a> .<br/>More information and alternatives about<br/>donation can be found <a href=\"https://librazik.tuxfamily.org/base-site-LZK/english.php#donation\"><span style=\" text-decoration: underline; color:#0986d3;\">here</span></a>.</p></body></html>"))
        self.labelTypeOfTheDayTitle.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:696;\">Tip Of The Day<br/>________________</span></p></body></html>"))
        self.labelTipOfTheDay.setText(_translate("Dialog", "<html><head/><body><p>Do you know the <span style=\" font-weight:600;\">ALT+F2</span> shortcut?</p><p>This shortcut allows you to start any software<br/>very quickly by simply typing its name.</p><p>This way you don\'t have to create many and<br/>many shortcuts on the desktop.</p></body></html>"))
        self.checkBox.setText(_translate("Dialog", "Do not show this message again"))

import resources_rc
