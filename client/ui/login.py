# Form implementation generated from reading ui file './ui/login.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlg_login(object):
    def setupUi(self, dlg_login):
        dlg_login.setObjectName("dlg_login")
        dlg_login.resize(294, 122)
        self.gridLayout = QtWidgets.QGridLayout(dlg_login)
        self.gridLayout.setObjectName("gridLayout")
        self.le_password = QtWidgets.QLineEdit(parent=dlg_login)
        self.le_password.setObjectName("le_password")
        self.gridLayout.addWidget(self.le_password, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=dlg_login)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=dlg_login)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le_username = QtWidgets.QLineEdit(parent=dlg_login)
        self.le_username.setObjectName("le_username")
        self.gridLayout.addWidget(self.le_username, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_cancel = QtWidgets.QPushButton(parent=dlg_login)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.btn_login = QtWidgets.QPushButton(parent=dlg_login)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout.addWidget(self.btn_login)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.retranslateUi(dlg_login)
        QtCore.QMetaObject.connectSlotsByName(dlg_login)

    def retranslateUi(self, dlg_login):
        _translate = QtCore.QCoreApplication.translate
        dlg_login.setWindowTitle(_translate("dlg_login", "Login"))
        self.label_2.setText(_translate("dlg_login", "Password"))
        self.label.setText(_translate("dlg_login", "Username"))
        self.btn_cancel.setText(_translate("dlg_login", "Cancel"))
        self.btn_login.setText(_translate("dlg_login", "Login"))
