# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
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
        Dialog.resize(640, 515)
        self.pb_send = QtGui.QPushButton(Dialog)
        self.pb_send.setGeometry(QtCore.QRect(368, 411, 112, 34))
        self.pb_send.setObjectName(_fromUtf8("pb_send"))
        self.le = QtGui.QLineEdit(Dialog)
        self.le.setGeometry(QtCore.QRect(81, 414, 271, 27))
        self.le.setObjectName(_fromUtf8("le"))
        self.pb = QtGui.QPushButton(Dialog)
        self.pb.setGeometry(QtCore.QRect(20, 410, 41, 34))
        self.pb.setObjectName(_fromUtf8("pb"))
        self.le_ip = QtGui.QLineEdit(Dialog)
        self.le_ip.setGeometry(QtCore.QRect(80, 470, 281, 27))
        self.le_ip.setObjectName(_fromUtf8("le_ip"))
        self.rb_s = QtGui.QRadioButton(Dialog)
        self.rb_s.setGeometry(QtCore.QRect(501, 71, 80, 25))
        self.rb_s.setObjectName(_fromUtf8("rb_s"))
        self.rb_c = QtGui.QRadioButton(Dialog)
        self.rb_c.setGeometry(QtCore.QRect(501, 105, 75, 25))
        self.rb_c.setObjectName(_fromUtf8("rb_c"))
        self.lv = QtGui.QListWidget(Dialog)
        self.lv.setGeometry(QtCore.QRect(40, 30, 441, 351))
        self.lv.setObjectName(_fromUtf8("lv"))
        self.pb_connect = QtGui.QPushButton(Dialog)
        self.pb_connect.setGeometry(QtCore.QRect(380, 470, 101, 34))
        self.pb_connect.setObjectName(_fromUtf8("pb_connect"))
        self.graphicsView = QtGui.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 641, 521))
        self.graphicsView.setStyleSheet(_fromUtf8("border-image: url(:/newPrefix/back.jpg) 0 0 0 0 stretch stretch;"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView_2 = QtGui.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 641, 531))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.graphicsView_2.raise_()
        self.graphicsView.raise_()
        self.pb_send.raise_()
        self.le.raise_()
        self.pb.raise_()
        self.le_ip.raise_()
        self.rb_s.raise_()
        self.rb_c.raise_()
        self.lv.raise_()
        self.pb_connect.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pb_send.setText(_translate("Dialog", "Send", None))
        self.pb.setText(_translate("Dialog", "...", None))
        self.rb_s.setText(_translate("Dialog", "Server", None))
        self.rb_c.setText(_translate("Dialog", "Client", None))
        self.pb_connect.setText(_translate("Dialog", "Connect", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

