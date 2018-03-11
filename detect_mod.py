import sys
from detect_auto import *
import speech_sign as ss
import classify_webcam as cw
import login_mod
import sign_english_mod as se
import chat_mod

class Detect(QtGui.QDialog):
    def __init__(self,parent=None,yes=None):
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pb_detect, QtCore.SIGNAL('clicked()'), self.run)
        QtCore.QObject.connect(self.ui.pb_login, QtCore.SIGNAL('clicked()'), self.login)
        QtCore.QObject.connect(self.ui.pb_send, QtCore.SIGNAL('clicked()'), self.send)
        if not(yes is None):
            if yes.rstrip() == "Yes":
                self.ui.rb2.setChecked(True)
            elif yes.rstrip() == "No":
                self.ui.rb1.setChecked(True)
    def send(self):
        c = chat_mod.Chat()
        c.show()
        c.exec_()
    def run(self):
        self.ui.label.setText("")
        if self.ui.rb1.isChecked():
            s = se.Sign()
            s.show()
            s.exec_()
        else:
            cw.main()
            with open("text.txt", "r") as f:
                self.ui.label.setText(f.read())

    def login(self):
        m = login_mod.Login()
        m.show()
        self.close()
        m.exec_()
if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    myapp=Detect()
    myapp.show()
    sys.exit(app.exec_())
