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
    result = float(exp[0]) / float(exp[1])

    if len(exp) == 2:
        return result

    for i in range(2, len(exp)):
        result = result / float(exp[i])
    return result


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
