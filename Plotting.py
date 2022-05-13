import matplotlib.pyplot as plt 
import numpy as np
import ErrorHandler
import re
import sys


class Plotter:

    def __init__(self,expression,minVal,maxVal):
        self.expression=ErrorHandler.validateExpresion(expression)
        self.minVal=ErrorHandler.validateInteger(minVal)
        self.maxVal=ErrorHandler.validateInteger(maxVal)
        ErrorHandler.validateMaxMinValues(minVal,maxVal)
   
   
    def func(self,x):
        return eval(self.expression)


    def CreatePoints(self):

        Xvalues=[]

        Yvalues=[]
        self.maxVal=self.maxVal+1

        testZeroDiv = ErrorHandler.validateDivisionByZero(self.expression, self.minVal, self.maxVal)

        for i in range(self.minVal, self.maxVal):

            Xvalues.append(i)
            if testZeroDiv == False and i == 0:
                Yvalues.append(float('inf'))
            else:    
                Yvalues.append(self.func(i))   

        return Xvalues,Yvalues        





    def draw(self):
        xList, yList = self.CreatePoints()
        plt.plot(xList, yList, color="blue", linewidth=1.5, label=self.expression)
        plt.title(self.expression)
        plt.xlabel("X")
        plt.ylabel("F(X)")
        plt.style.use("seaborn-darkgrid")
        plt.grid()
        plt.show()

        