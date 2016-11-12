import math

def Sum(a,b):
    sum=a+b
    return sum

def Product(a,b):
    product=a*b
    return product

def quotient(a,b):
    if b != 0:
        quotient=a/b
        return quotient
    else:
        print("The divisor cannot be 0 ")

def exponent(a,b):
    try:
        exponent=a**b
        return exponent
    except OverflowError:
        print("The number is too big ")

def productSum (a,b):
    result = 0.0
    for index in range(0,int(b)):
        result=result + a
    return result

def forloop1 (a,b):
    result=a
    for index in range(0,int(b)):
        result=result + 2
        print("My loop number is " + str(index+1) + " and my result is "  + str(result))
    return  result

def tableof2 ():
    result=2
    for index in range(1,11):
        result=2 *index
        print("My loop number is " + str(index) + " and my result is " + str(result))
    return result

def tableof7 ():
    result=7
    for index in range(1,11):
        result=7 *index
        print("My loop number is " + str(index) + " and my result is " + str(result))


