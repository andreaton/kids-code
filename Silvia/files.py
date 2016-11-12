from pathlib import Path

"""
file_name = 'file.txt'
file = Path(file_name)
number = 0
if file.is_file():
    with open(file_name) as f:
        for line in f:
            # print (line)
            number = line
            print(number)
    new_number = int(number) + 1
    text_file = open(file_name, 'w')
    text_file.writelines(str(new_number))
else:
    print("0")
    file_open = open(file_name, 'w')
    file_open.writelines("1")
"""

file_name='file2.txt'
file= Path(file_name)
number1=0
number2=0
if file.is_file():
    with open(file_name) as f:
        index = 0
        for line in f:
            index=index+1
            #print (line)
            if index==1:
                number1 =line
                print (number1)
            if index==2:
                number2=line
                print (number2)
    new_number1 = int(number1) + 1
    new_number2 = int(number2) - 1
    text_file = open(file_name, 'w')
    text_file.writelines (str(new_number1))
    text_file.writelines ("\n")
    text_file.writelines (str(new_number2))
    text_file.close()
else:
    print ("0")
    file_created=open(file_name, 'w')
    file_created.writelines("1")
    file_created.writelines ("\n")
    file_created.writelines("99")
    file_created.close()



