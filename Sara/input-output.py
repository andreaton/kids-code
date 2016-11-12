
# Get input from keyboard and save it into variable name
#name = input("What's your name? ")
#print("Nice to meet you " + name + "!!!!")
#age = input("Your age? ")

#print("So, you are are already " + str(age) + " years old, " + name + "!")

#print("So, you are are already " + age + " years old, " + name + "!")

file1 = open('c:\\temp\\pancakes.txt', 'r')
line = file1.readline()
print (line)

exit(0)
number1 = input ("give me a number ")
number2 = input ("give me another number ")

number3 = int(number1) + int(number2)
print ("sum of the two numbers is " + str(number3))

number4 = int(number1) - int(number2)
print ("the difference of the two numbers is " + str(number4))

number5 = int(number1) * int(number2)
print ("the product of the two numbers is " + str(number5))

number6 = int(number1) / int(number2)
print ("the quotient of the two numbers is " + str(number6))