import random

list_1=[1,2,3]
list_2=[4,5,6]
print (list_1)
print (list_2)

sum_list=[]
for x in range (0,len(list_1)):
    sum= list_1[x] + list_2[x]
    sum_list.append(sum)

print (str(sum_list))

onehundred_randoms=[]
onehundred_randoms2=[]
for x in range (0,100):
    onehundred_randoms.append(random.randrange(101))
    onehundred_randoms2.append(random.randrange(101))

onehundred_sum_list=[]
for x in range(0,len(onehundred_randoms)):
    list_sum= onehundred_randoms[x]+ onehundred_randoms2[x]
    onehundred_sum_list.append(list_sum)

max_value=onehundred_sum_list[0]
min_value=onehundred_sum_list[0]
max_local=0
min_local=0
for x in range(0,len(onehundred_sum_list)):
    if onehundred_sum_list[x]> max_value:
        max_value= onehundred_sum_list[x]
        max_local=x
    if onehundred_sum_list[x]< min_value:
        min_value= onehundred_sum_list[x]
        min_local=x


print (str(onehundred_randoms))
print(str(onehundred_randoms2))
print (str(onehundred_sum_list))

print ("The maximum value of the random lists' sums is "+ str(max_value)+ " and its location in the new list is "+ str(max_local))
print ("The minimum value of the random lists' sums is "+ str(min_value)+ " and its location in the new list is "+ str(min_local))
