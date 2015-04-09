"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
from arithmetic import *

def calculate():

    quit = False

    while not quit:
        ask = raw_input("> ")
        expression = ask.split(" ")
        symbol = expression[0]
        # checks the length of the expression
        if len(expression) == 2:
            opr = int(expression[1])
            # checks if the expression is a cube or a square
            if symbol == 'cube':
                print cube(opr)
                
            elif symbol == 'square':
                print square(opr)
            else:
                print "I don't understand"

        elif len(expression) >= 3:
            opr1 = float(expression[1])
            opr2 = float(expression[2])
            lst_num = expression[1:]

            if symbol == 'pow':
                print pow(opr1, opr2)

            elif symbol == 'mod':
                print mod(opr1, opr2)
            
            elif symbol == '+':
                print add(lst_num)
            elif symbol == '-':
                print subtract(lst_num)
            elif symbol == '*':
                print multiply(lst_num)
            elif symbol == '/':
                print divide(lst_num)
            else:
                print "I don't understand"

        else:
            if len(expression) == 1 and expression[0] == "q":
                quit = True
                break
            print "I don't understand"


calculate()



