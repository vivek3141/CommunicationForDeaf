import sys
from chat_auto import *
import socket
import cv2
import classify_webcam as cw

class Chat(QtGui.QDialog):
    def __init__(self,parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        with open("text.txt","r") as f:
            t = f.read()
        self.ui.le.setText(t)
        QtCore.QObject.connect(self.ui.pb_send, QtCore.SIGNAL('clicked()'), self.main)
        QtCore.QObject.connect(self.ui.rb_c, QtCore.SIGNAL('clicked()'), self.rb2)
        QtCore.QObject.connect(self.ui.rb_s, QtCore.SIGNAL('clicked()'), self.rb1)
        QtCore.QObject.connect(self.ui.pb_connect, QtCore.SIGNAL('clicked()'), self.connect)
        QtCore.QObject.connect(self.ui.pb, QtCore.SIGNAL('clicked()'), self.sign)
        self.s = None
        self.c = None
        with open("login.txt", "r") as f:
            self.y = f.read()
    def sign(self):
        cw.main()
        with open("text.txt", "r") as f:
            self.ui.le.setText(f.read())
    def connect(self):
        if self.ui.rb_c.isChecked():
            self.connect_c()
            return False
        elif self.ui.rb_s.isChecked():
            self.connect_s()
            return False
        else:
            QtGui.QMessageBox.warning(self, "Warning", "Please select server or client!")
    def connect_s(self):
        self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.c.bind(("", 50008))
        self.server()
    def connect_c(self):
        host = self.ui.le_ip.text()
        if(host == ""):
            QtGui.QMessageBox.warning(self, "Warning", "Please enter ip!")
            return False
        port = 50008

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        self.ui.lv.addItem("Connected to " + (host) + " on port " + str(port))
    def main(self):
        if self.ui.rb_c.isChecked():
            self.send()
            return False
        elif self.ui.rb_s.isChecked():
            self.server()
            return False
        else:
            QtGui.QMessageBox.warning(self, "Warning", "Please select server or client!")
    def server(self):
        if self.c is None:
            QtGui.QMessageBox.warning(self, "Warning", "Please connect!")
            return False

        self.c.listen(1)
        print("Trying")
        self.conn, addr = self.c.accept()
        self.ui.lv.addItem("Connection from " + str(addr[0]))
        data = self.conn.recv(1024)
        self.ui.lv.addItem("Recieved: " + (data.decode()))
        self.conn.sendall(self.ui.le.text().encode())
    def rb1(self):
        self.ui.le_ip.hide()

    def rb2(self):
        self.ui.le_ip.show()

    def send(self):
        if self.ui.rb_s.isChecked():
            self.conn.sendall(self.ui.le.text().encode())
        if self.s is None:
            QtGui.QMessageBox.warning(self, "Warning", "Please connect!")
        inp = self.ui.le.text()
        self.s.sendall(inp.encode())
        self.ui.lv.addItem("Sent: "+inp)
        data = self.s.recv(1024)
        self.ui.lv.addItem("Recieved: " + (data.decode()))
        if self.y == "Yes":
            for i in data.decode().rstrip():
                if i == " ":
                    continue
                img = cv2.imread(".\Letters\\" + str(i).upper() + ".PNG")
                if img is None:
                    print(":" + i)
                height, width = img.shape[:2]
                img = cv2.resize(img, (int(width * 2), int(height * 2)), interpolation=cv2.INTER_AREA)
                cv2.imshow('image', img)
                cv2.waitKey(1000)
                cv2.destroyAllWindows()

         
if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    myapp=Chat()
    myapp.show()
    sys.exit(app.exec_()) 
