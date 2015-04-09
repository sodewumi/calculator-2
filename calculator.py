"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
from arithmetic import *

def calculate():

    ask = raw_input("> ")
    expression = ask.split(" ")
    symbol = expression[0]
    # checks the length of the expression
    if len(expression) == 2:
        opr = int(expression[1])
        # checks if the expression is a cube or a square
        if symbol == 'cube':
            return cube(opr)
            
        elif symbol == 'square':
            return square(opr)
        else:
            return "I don't understand"

    elif len(expression) == 3:
        opr1 = int(expression[1])
        opr2 = int(expression[2])
        if symbol == 'pow':
            return pow(opr1, opr2)

        elif symbol == 'mod':
            return mod(opr1, opr2)
        
        elif symbol == '+':
            return add(opr1, opr2)
        elif symbol == '-':
            return substract(opr1, opr2)
        elif symbol == '*':
            return multiply(opr1, opr2)
        elif symbol == '/':
            return divide(opr1, opr2)
        else:
            return "I don't understand"

    # else:
        # the array doen't have a length of 2 or 3
        # return "I don't understand"
    return expression

print(calculate())



