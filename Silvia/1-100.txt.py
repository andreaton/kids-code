
mylist=list(range(1,101))
oddlist=list()
evenlist=list()
fivelist=list()
sevenlist=list()
threelist=list()

randomvariable="hello everybody"

for number in mylist:
    #print ("This is count " + str(number))
    if (number % 2 == 0):
        evenlist.append(number)
    if (number % 5 == 0):
        fivelist.append(number)
    if (number % 2 !=0):
        oddlist.append(number)
    if (number % 7 == 0):
        sevenlist.append(number)
    if (number % 3 == 0):
        threelist.append(number)


print (str(evenlist))
print(str(oddlist))
print (str(fivelist))
print (str(sevenlist))
print (str(threelist))

text_file = open("1-40_list.txt","w")
text_file.writelines(str(evenlist))
text_file.write("\n")
text_file.write("im Silvia")
text_file.write("\n")
text_file.write(randomvariable+"\n")
text_file.writelines(str(oddlist))
text_file.close()

