# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(443, 284)
        self.le_login = QtGui.QLineEdit(Dialog)
        self.le_login.setGeometry(QtCore.QRect(40, 80, 361, 41))
        self.le_login.setObjectName(_fromUtf8("le_login"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 20, 231, 41))
        self.label.setStyleSheet(_fromUtf8("font: 16pt \"Segoe UI\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.pb_login = QtGui.QPushButton(Dialog)
        self.pb_login.setGeometry(QtCore.QRect(150, 150, 141, 51))
        self.pb_login.setStyleSheet(_fromUtf8("font: 16pt \"Segoe UI\";"))
        self.pb_login.setObjectName(_fromUtf8("pb_login"))
        self.pb_signup = QtGui.QPushButton(Dialog)
        self.pb_signup.setGeometry(QtCore.QRect(170, 230, 101, 34))
        self.pb_signup.setStyleSheet(_fromUtf8("font: 8pt \"Segoe UI\";"))
        self.pb_signup.setObjectName(_fromUtf8("pb_signup"))
        self.cb_r = QtGui.QCheckBox(Dialog)
        self.cb_r.setGeometry(QtCore.QRect(300, 160, 151, 25))
        self.cb_r.setObjectName(_fromUtf8("cb_r"))
        self.graphicsView = QtGui.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 451, 291))
        self.graphicsView.setStyleSheet(_fromUtf8("border-image: url(:/newPrefix/back.jpg) 0 0 0 0 stretch stretch;"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView.raise_()
        self.le_login.raise_()
        self.label.raise_()
        self.pb_login.raise_()
        self.pb_signup.raise_()
        self.cb_r.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Login", None))
        self.label.setText(_translate("Dialog", "Login ID", None))
        self.pb_login.setText(_translate("Dialog", "Login", None))
        self.pb_signup.setText(_translate("Dialog", "Sign Up", None))
        self.cb_r.setText(_translate("Dialog", "Remember Me", None))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

