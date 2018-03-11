# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_english.ui'
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
        Dialog.resize(548, 417)
        self.te = QtGui.QTextEdit(Dialog)
        self.te.setGeometry(QtCore.QRect(40, 100, 381, 261))
        self.te.setObjectName(_fromUtf8("te"))
        self.pb_trans = QtGui.QPushButton(Dialog)
        self.pb_trans.setGeometry(QtCore.QRect(430, 100, 112, 34))
        self.pb_trans.setObjectName(_fromUtf8("pb_trans"))
        self.pb_record = QtGui.QPushButton(Dialog)
        self.pb_record.setGeometry(QtCore.QRect(360, 20, 71, 61))
        self.pb_record.setStyleSheet(_fromUtf8("border-image: url(:/newPrefix/record.png) 0 0 0 0 stretch stretch;"))
        self.pb_record.setText(_fromUtf8(""))
        self.pb_record.setObjectName(_fromUtf8("pb_record"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 261, 21))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.graphicsView = QtGui.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 551, 421))
        self.graphicsView.setStyleSheet(_fromUtf8("border-image: url(:/newPrefix/back.jpg) 0 0 0 0 stretch stretch;"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView.raise_()
        self.te.raise_()
        self.pb_trans.raise_()
        self.pb_record.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Translate", None))
        self.pb_trans.setText(_translate("Dialog", "Translate", None))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

