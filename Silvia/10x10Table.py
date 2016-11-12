import sys

def TenxTenTable():
    number=0
    for x in range (0,10):
        for x in range (0,10):
            number = number+1
            sys.stdout.write (str(number)+" ")
        print ("")


def TenxTenFile(text_file):
    number = 0
    for x in range(0, 10):
        for x in range(0, 10):
            number = number + 1
            text_file.writelines(str(number) + " ")
        text_file.writelines ("\n")

def TenxTenFilex2 (text_file):
    number = 0
    for x in range(0,5):
        for x in range(0,10):
            number = number + 2
            text_file.writelines(str(number) + " ")
        text_file.writelines ("\n")

def TenxTenFilex3 (text_file):
    number = 0
    for x in range(0,10):
        for x in range(0,10):
            number = number + 3
            if number > 100:
                return number
            text_file.writelines(str(number) + " ")
        text_file.writelines ("\n")

def TenxTenFilex5 (text_file):
    number = 0
    for x in range(0,10):
        for x in range(0,10):
            number = number + 5
            if number > 100:
                return number
            text_file.writelines(str(number) + " ")
        text_file.writelines ("\n")


file_name="TimesTablesto100.txt"
text_file=open(file_name, "w")

TenxTenFile(text_file)
text_file.writelines("\n")
TenxTenFilex2(text_file)
text_file.writelines("\n")
TenxTenFilex3(text_file)
text_file.writelines("\n")
TenxTenFilex5(text_file)

text_file.close ()

even=0
odd=0
with open(file_name) as f:
    for line in f:
        #print (line.rstrip())
        for word in line.split():
            if int(word)%2==0:
                even=even+1
            else:
                odd=odd+1
print ("There are "+str(even)+" even numbers and "+str(odd)+" odd numbers in the text file")


text_file.close ()


