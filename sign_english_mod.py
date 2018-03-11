import sys
from sign_english_auto import *
import cv2
import speech_recognition as sr
 
class Sign(QtGui.QDialog):
    def __init__(self,parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pb_record, QtCore.SIGNAL('clicked()'), self.sign)
        QtCore.QObject.connect(self.ui.pb_trans, QtCore.SIGNAL('clicked()'), self.trans)

    def sign(self):
        self.ui.label.setText("")
        text = ""
        r = sr.Recognizer()

        with sr.Microphone(device_index=0, sample_rate=48000,
                           chunk_size=2048) as source:
            r.adjust_for_ambient_noise(source)
            print("say")

            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                self.ui.te.setText(str(text))
                pass
            except sr.UnknownValueError:
                self.ui.label.setText("Can't Understand")
                return False
            except sr.RequestError as e:
                self.ui.label.setText("Can't connect to the internet")
                return False
        self.ui.label.setText("")
    def trans(self):
        for i in self.ui.te.toPlainText().rstrip():
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
    myapp=Sign()
    myapp.show()
    sys.exit(app.exec_()) 
