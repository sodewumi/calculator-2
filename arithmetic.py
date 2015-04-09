def add(exp):
    sum = 0
    for i in exp:
        sum += float(i)
    return sum


def subtract(exp):
    minus = 0
    for i in exp:
        minus -= float(i)
    return minus 


def multiply(exp):
    mult = 1
    for i in exp:
        mult *= float(i)
    return mult


def divide(exp):
    pre_div = None
    div = 1
    for i in range(0, len(exp)-1):
        if pre_div == None:
            div = float(exp[i]) / float(exp[i+1])
            pre_div = div
        else:
            div = (pre_div / float(exp[i])) / float(exp[i+1])
    return div


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2
