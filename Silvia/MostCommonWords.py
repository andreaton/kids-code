
import collections

def Word_frequency(filename):
    dic = collections.Counter()
    with open (filename) as f:
        for line in f:
            for word in line.split():
                # if word is all  capital, skip it
                if len(word) > 3:
                    if word[0].isupper() and word[1].isupper() and word[2].isupper():
                        continue
                word = "".join(c for c in word if c not in ('!', '.', ':', ',','?',';','-'))
                if word[-1]=="'":
                    word=word[:-1]
                dic[word.lower()] += 1
    return dic

def file_filter(filename):
    list=[]
    with open(filename) as f:
        for line in f:
            #print (line)
            index=0
            for word in line.split():
                index=index+1
                if index==2:
                   list.append(word.lower())
    return list


#for each element of list a check if it is present in list b
#it returns a list of what is not included in list b
def CompareLists (listA,listB):
    listC=[]
    for i in listA:
        if i in listB:
            continue
        else:
            listC.append(i)
    return listC

cleopatra_file="cleopatra.txt"
common_words_unclean="listnotclean.txt"
common_words=[]

tragedy_file=open(cleopatra_file)
tragedy_file.close()

cleopatra_dic = Word_frequency(cleopatra_file)
common_words_list=(file_filter(common_words_unclean))


file_name="Most_Common_Words_English.txt"
most_common_words_file =open(file_name,"w")
for x in common_words_list:
    most_common_words_file
    most_common_words_file.writelines(x+"\n")


UncommonWords=CompareLists(cleopatra_dic,common_words_list)
print (UncommonWords)
print (len("In book  found " + UncommonWords + " uncommon words"))


