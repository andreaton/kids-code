import math
import random


#is_number makes sure that a variable is a number
#input: number
#ouput: True if it is number, False if not
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#  input: 2 numbers
#  output: number
#  What it does: returns the sum of the numbers
def AddNumbers(a,b):
    if not is_number(a):
        return ValueError ('ERROR: AddNumbers(a,b):The first parameter is not a number')
    if not is_number(b):
        return ValueError ('ERROR: AddNumbers(a,b):The second parameter is not a number')
    return a+b

#  input: 2 numbers
#  output: number
#  What it does: return the multiplication of the numbers
def MultiplyNumbers(a,b):
    if not is_number(a):
       return ValueError ('ERROR: MultiplyNumbers(a,b):The first parameter is not a number')
    if not is_number(b):
        return ValueError ('ERROR: MultiplyNumbers(a,b):The second parameter is not a number')
    return a*b

# input: number
# output: number
# What it does: return sum of all numbers from 0 leading up to designated number
def NumberSeries(n):
    sum=0
    if is_number(n):
        n=math.trunc (n)
        for x in range(0, n+1):
            sum=sum+x
        return sum
    else:
        return 0

# input: none
# output: 2 numbers
# What it does: gets 3 numbers and find ax**2+bx+c
def SecondoGrado():
    print("i will preform the equation ax^2+bx+c=0")
    a = input("give me value a ")
    b = input("give me value b ")
    c = input("give me value c ")

    a = float(a)
    b = float(b)
    c = float(c)

    if (b ** 2 - 4 * a * c) >= 0:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        print("these are your solutions:")
        print(x1)
        print(x2)

    else:
        print("no real solution")

# input: 3 numbers
# output: 2 numbers
# What it does: gets 3 numbers and find ax**2+bx+c
def SecondoGrado1 (a,b,c):

    if(b**2-4*a*c)>=0:
        x1=(-b+math.sqrt(b**2-4*a*c))/2*a
        x2=(-b-math.sqrt(b**2-4*a*c))/2*a
        print("these are your solutions:")
        print(x1)
        print(x2)

    else:
        print("no real solution")

# input: 2 numbers
# output: 1 number
# What it does: find the are of a triangle using given side lengths
def TriangoloArea (base,height):
    areaTemp=float(base)*float(height)/2
    return areaTemp

def TriangoloPer (side1,side2,side3):
    per=float(side1)+float(side2)+float(side3)
    return per

def DivideNumbers (a,b):
    if not is_number(a):
        return ValueError ('ERROR: DivideNumbers(a,b): The first parameter is not a number')
    if not is_number(b):
        return ValueError ('ERROR: DivideNumbers(a,b): The second parameter is not a number')
    if b==0:
        return ValueError ('ERROR: DivideNumbers(a,b): I cannot divide by 0')
    return a/b

def Exponents(a,b):
    result=1
    if b==0:
        return 1
    else:
        for x in range (0,b):
            result=result*a
    return result

def Factorial (n):
    product=1
    if n==0:
        return 1
    else:
        for x in range(0,n):
            product=product*(x+1)
    return product

def Sum(z):
    n=0
    if z==0:
        return 0
    else:
        for x in range (0,z):
            n=n+x+1
    return n

def Dice():
    return random.randint (1,6)

def GuessTheDice():
    for count in range(0,5):
        guess = input("Give me your guess between 1 and 6: ")
        if not is_number(guess):
            print("Mistake! Not a number")
        else:
            break
    x = Dice()
    print("Dice:" + str(x))
    if float(guess) == float(x):
        print("You win!")
        return 1
    else:
        print("You lose.")
        return 0

def Generate123():
    return random.randint (1,3)

def Guess123():
    for count in range(0,5):
        guess = input("Give me your guess between 1,2, and 3: ")
        if not is_number(guess):
            print("Mistake! Not a number")
        else:
            break
    x = Generate123()
    print("Dice:" + str(x))
    if int(guess) == int(x):
        print("You win!")
        return 1
    else:
        print("You lose.")
        return 0
