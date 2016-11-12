
list_1=[1,3,5,7,13]
sub_list=[3,5,7]
sub_list2=[2,3,7]

def FindSublist(a,b):
    for i in b:
        if i in a:
            continue
        else:
            return False

print (str(FindSublist(list_1,sub_list2)))


