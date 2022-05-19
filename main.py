from pyclbr import Function
import string
from tkinter import messagebox
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QWidget, QDialog,QMainWindow,QLineEdit,QPushButton,QApplication,QGridLayout, QMessageBox
from ErrorHandler import *
from Plotting import *
import sys

class UI(QMainWindow):
    def __init__(self):
        self.lineEditFocused=None
        super(UI, self).__init__()
        uic.loadUi('Interface.ui', self)
        self.show()
        self.setWindowTitle("Function Plotter")
        self.setWindowIcon(QtGui.QIcon('Images\icons8-stocks-50.png'))
        self.Plot_Button.clicked.connect(self.plot)
        self.INFO.clicked.connect(self.ShowInfo)  
        self.One.clicked.connect(lambda:self.SetFocusText1("1"))
        self.Two.clicked.connect(lambda:self.SetFocusText1("2"))
        self.Three.clicked.connect(lambda:self.SetFocusText1("3"))
        self.Four.clicked.connect(lambda:self.SetFocusText1("4"))
        self.Five.clicked.connect(lambda:self.SetFocusText1("5"))
        self.Six.clicked.connect(lambda:self.SetFocusText1("6"))
        self.Seven.clicked.connect(lambda:self.SetFocusText1("7"))
        self.Eight.clicked.connect(lambda:self.SetFocusText1("8"))
        self.Nine.clicked.connect(lambda:self.SetFocusText1("9"))
        self.Zero.clicked.connect(lambda:self.SetFocusText1("0"))
        self.Mul.clicked.connect(lambda:self.SetFocusText1("*"))
        self.division.clicked.connect(lambda:self.SetFocusText1("/"))
        self.Addition.clicked.connect(lambda:self.SetFocusText1("+"))
        self.Subtract.clicked.connect(lambda:self.SetFocusText1("-"))
        self.X.clicked.connect(lambda:self.SetFocusText1("x"))
        self.power.clicked.connect(lambda:self.SetFocusText1("^"))
        self.Delete.clicked.connect(self.DltBtn)
        self.Clear.clicked.connect(self.Clearbtn)
       
    def SetFocusText1(self,val):
            smalltext=str(val)
            text=self.Expression.text()   
            self.Expression.setText(text+smalltext)    

    def ShowInfo(self):
        msg = QMessageBox()
        msg.setText("-The following operators are supported: + - / * ^ \n\n\n-The expression of the function must be in the format of\n 5*x^3 + 2*x\n \n-Keyboard is for the function only,because some of keys will be invalid in min and max fields")
        msg.setWindowTitle("Info")
        msg.setWindowIcon(QtGui.QIcon("Images\icons8-info-50.png"))
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
   
    def DltBtn(self):
        testtext=self.Expression.text()
        if(len(testtext)>0):
           length=len(testtext)-1
           testtext=testtext[0:length]
           self.Expression.setText(testtext)

    def Clearbtn(self):
        self.Expression.setText("")      

    def plot(self):
       try:
            plot=Plotter(self.Expression.text(),self.MinVal.text(),self.MaxVal.text())
            plot.draw()

       except ValueError as errormsg:
            err=errormsg.args[0]
            msg = QMessageBox()
            msg.setText(err)
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QtGui.QIcon("Images\icons8-error-50.png"))
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            return    
  
if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    currWindow = UI()
    sys.exit(application.exec_())