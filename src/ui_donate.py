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
        Dialog.resize(426, 412)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelDonate = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDonate.sizePolicy().hasHeightForWidth())
        self.labelDonate.setSizePolicy(sizePolicy)
        self.labelDonate.setOpenExternalLinks(True)
        self.labelDonate.setObjectName("labelDonate")
        self.verticalLayout.addWidget(self.labelDonate)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
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
        Dialog.setWindowTitle(_translate("Dialog", "Give For Librazik "))
        self.labelDonate.setText(_translate("Dialog", "<html><head/><body><p>Thanks to use LIBRAZIK !</p><p>You seems to be a regular LIBRAZIK user.<br/>Create and maintain this distribution is a hard work that takes time.<br/>That is why donations (even small) are really appreciated.</p><p>You can donate <a href=\"https://liberapay.com/LibraZiK/donate\"><span style=\" text-decoration: underline; color:#2980b9;\">here</span></a> .</p></body></html>"))
        self.labelTypeOfTheDayTitle.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:696;\">Tip Of The Day<br/>________________</span></p></body></html>"))
        self.labelTipOfTheDay.setText(_translate("Dialog", "<html><head/><body><p>Do you know <span style=\" font-weight:600;\">ALT+F2</span> shortcut ?</p><p><br/>This shortcut allows you to start very quicky<br/>any software by typing its name.</p><p>This way, you don\'t have to create many and many<br/>shortcuts on the desktop.</p></body></html>"))
        self.checkBox.setText(_translate("Dialog", "Do not show this message again"))

