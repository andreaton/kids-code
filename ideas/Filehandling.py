import os
import collections
import string
# Open a file
filename=input("Give  me the name of the file you want me to read")

#fo = open(filename, "wb")
#print ("Name of the file: ", fo.name)
#print ("Closed or not : ", fo.closed)
#print ("Opening mode : ", fo.mode)
#fo.close()

contents = open(filename).read()
words = contents.split()
print ("The words I found are:", words, "__END_OF_WORDS__")
words.sort()
print ("The sorted list is: ", words)
print ("This is the frequency of the words:",collections.Counter(words))
exclude = set(string.punctuation)
for i in range(len(words)):
    words[i] = ''.join(ch for ch in words[i] if ch not in exclude)
print ("!!New sorted list modified: ", words)
print ("This is the frequency of the MODIFIED words:",collections.Counter(words))
#line = line.translate(None, '!@#$')

#contents = open(filename)
#lines = contents.readline()
#lines.sort()
#print ("The content of the file ", filename , " is: ", contents,"__END_OF_FILE__" )