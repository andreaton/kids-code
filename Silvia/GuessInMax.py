import random
import sys


print ("Do you want to play a guessing game?[y]es or [n]o")
yesno=sys.stdin.read(2)

if yesno.rstrip()=="y":
    print ("Great, you want to play!")
    max=input("Give me a maximum number")
    print ("Now I will choose a number between 0 and "+str(max)+". You have to guess what the number is. You have 10 tries.")
    winningnumber = random.randint(0, int(max))
    for x in range (0,10):
        guess=input ("Give me your guess")
        if int(guess)==winningnumber:
            print ("Great! You guessed that I chose "+str(winningnumber)+", and you were correct!")
            break
        elif int(guess)>winningnumber+10:
            print ("You are to high. Choose a lower number.")
        elif int(guess)<winningnumber-10:
            print ("You are to low. Choose a higher number.")


else:
    print ("Too bad, it would have been fun.")

print (str(winningnumber))