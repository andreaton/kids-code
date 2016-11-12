import MathFunctions
import sys

print ("Do you want to play a dice game?([y]es/[n]o)")
yesno=sys.stdin.read(2)

if yesno.rstrip()=="y":
    total = 0
    print("Great you want to play!")
    for x in range (0,10):
        game=MathFunctions.GuessTheDice()
        total=total+game
    print ("You scored "+str(total)+"/10")
    if total>5:
        print ("You won the game!")
    elif total<5:
        print ("You lost the game.")
    else:
        print ("It was a tie.")

else:
    print ("Too bad, you are missing out.")
