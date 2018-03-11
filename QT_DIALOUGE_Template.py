import sys
from Sale_calc_auto import * 
 
class MyForm(QtGui.QDialog):
    def __init__(self,parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self) 
 
        #this is where we will bind the event handlers 
         
#This is where we will insert the functions (defs) 
         
if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_()) 
