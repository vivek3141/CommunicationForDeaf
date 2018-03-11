# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detect.ui'
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
        Dialog.resize(497, 368)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(330, 20, 151, 80))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.rb1 = QtGui.QRadioButton(self.groupBox)
        self.rb1.setGeometry(QtCore.QRect(10, 20, 124, 25))
        self.rb1.setObjectName(_fromUtf8("rb1"))
        self.rb2 = QtGui.QRadioButton(self.groupBox)
        self.rb2.setGeometry(QtCore.QRect(10, 50, 124, 25))
        self.rb2.setObjectName(_fromUtf8("rb2"))
        self.pb_detect = QtGui.QPushButton(Dialog)
        self.pb_detect.setGeometry(QtCore.QRect(100, 120, 291, 151))
        self.pb_detect.setObjectName(_fromUtf8("pb_detect"))
        self.pb_login = QtGui.QPushButton(Dialog)
        self.pb_login.setGeometry(QtCore.QRect(20, 20, 112, 34))
        self.pb_login.setObjectName(_fromUtf8("pb_login"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 300, 421, 41))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Detect", None))
        self.rb1.setText(_translate("Dialog", "Eng to ASL", None))
        self.rb2.setText(_translate("Dialog", "ASL to Eng", None))
        self.pb_detect.setText(_translate("Dialog", "Detect", None))
        self.pb_login.setText(_translate("Dialog", "Login", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

