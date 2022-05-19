import re
import sys


    
def validateExpresion(expression):
    expression = expression.replace(" ", "")
    if expression == "":
        raise ValueError("Empty Function")
    toMatch = "(-)?(\d+$)|((-)?(\d+[+-])?(\d+[\*\/])?[xX](\^\d+)?([+-](\d+)?([\*\/][xX](\^\d+)?)?)*)*$"
    matched = re.match(toMatch, expression)
    if not matched:
        raise ValueError("Invalid Expression, it must be like the expression in the info")
        print("error")
    
    expression = expression.replace('^', '**').replace('X', 'x')
    
    return expression
#-------------------------------------------------------------------------------------
def validateInteger(strNum):
    try:
        num = int(strNum)
        return num
    except:
         if(strNum==""):
               raise ValueError("There is an empty field")
         else:      
               raise ValueError("It's not a number")
#-------------------------------------------------------------------------------------    
def validateMaxMinValues(minVal, maxVal):
    if float(minVal) >= float(maxVal):
        raise ValueError("Maximum must be greater than Minimum")
#-------------------------------------------------------------------------------------
def validateDivisionByZero(expression, minVal, maxVal):
    if expression.find('/X') != -1 or expression.find('/x') != -1 and minVal <= 0 and maxVal >= 0:
        return False
    return True
