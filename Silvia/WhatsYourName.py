import random
import math
import sys

def Generate123():
    return random.randint (1,3)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

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

def MomsGame():
    for count in range(0,5):
        guess = input("Give me your guess between 1,2, and 3: ")
        if not is_number(guess):
            print("Mistake! Not a number")
        else:
            break
    print ("Dice: "+ str(guess))
    print ("You win!")
    return 1


print ("Do you want to play a guessing game?([y]es/[n]o)")
yesno=sys.stdin.read(2)

if yesno.rstrip()=="y":
    result=0
    print ("Great, you want to play!")
    name=input ("What are your initials? ")
    if name.lower()=="rlt" or name.lower()=="rt":
        for x in range (0,10):
            winningnumber = MomsGame()
            result=result+ winningnumber
        print ("You scored " + str(result)+"/10")
    else:
        total = 0
        for x in range(0, 10):
            game = Guess123()
            total = total + game
        print("You scored " + str(total) + "/10")
        if total > 5:
            print("You won the game!")
        elif total < 5:
            print("You lost the game.")
        else:
            print("It was a tie.")


else:
    print ("Too bad, you are missing out.")

