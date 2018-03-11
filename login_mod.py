import sys
from PyQt4 import QtCore, QtGui, uic
import sqlite3
from login_auto import *
import detect_mod
import sign_mod
  

class Login(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pb_login, QtCore.SIGNAL('clicked()'), self.login)
        QtCore.QObject.connect(self.ui.pb_signup, QtCore.SIGNAL('clicked()'), self.sign)

    def sign(self):
        m = sign_mod.Sign(None)
        m.show()
        self.close()
        m.exec_()

    def login(self):
        t = self.ui.le_login.text()
        o = sqlite3.connect("data.db")
        cur = o.cursor()
        try:
            cur.execute("select ab from username where username='" + str(t)+"'")
        except sqlite3.Error as e:
            print(e)
        l = cur.fetchall()
        print(l)
        try:
            y = str(l[0][0])
        except IndexError:
            QtGui.QMessageBox.warning(self, "Warning!",  "No such username!")
            return False
        print(y)
        if self.ui.cb_r.isChecked():
            with open("login.txt","w") as f:
                f.write(y)
        m = detect_mod.Detect(yes=y)
        m.show()
        self.close()
        m.exec_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = Login(None)
    myWindow.show()
    app.exec_()
