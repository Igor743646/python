import sys

# Импортируем наш интерфейс
from styles import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import QRect, Qt


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку         
        # self.ui.progressBar.setProperty("value", len(self.ui.textEdit.toPlainText()))
        self.ui.pushButton.clicked.connect(self.DomainCheck)          
        


    def DomainCheck(self):
    	
    	stroka1 = self.ui.textEdit.toPlainText()
    	stroka2 = self.ui.textEdit_2.toPlainText()

    	print ("Письмо было отправленно по адрессу: " + stroka2)

    	self.ui.textEdit.setText("")
    	self.ui.textEdit_2.setText("")

if __name__=="__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())