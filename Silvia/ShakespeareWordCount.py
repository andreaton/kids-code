
import collections

comedy_file_name="comedy_of_errors.txt"
tragedy_file_name="cleopatra.txt"

def Word_count_Anthony_and_Cleopatra():
    #tragedy_file_name="cleopatra.txt"
    tragedy_file=open(tragedy_file_name)
    tragedy_file.close()

    total_words_tragedy = 0
    with open (tragedy_file_name) as f:
        for line in f:
            for word in line.split():
                total_words_tragedy = total_words_tragedy + 1

    print ("There are "+str(total_words_tragedy)+" words in Shakespeare's Anthony and Cleopatra")

def Word_count_Comedy_of_Errors():
    #comedy_file_name="comedy_of_errors.txt"
    comedy_file=open(comedy_file_name)
    comedy_file.close()

    total_words_comedy = 0
    with open (comedy_file_name) as f:
        for line in f:
            for word in line.split():
                total_words_comedy = total_words_comedy + 1

    print ("There are "+str(total_words_comedy)+" words in Shakespeare's Comedy of Errors")

def Word_count(filename):
    total_words = 0
    with open (filename) as f:
        for line in f:
            for word in line.split():
                total_words = total_words + 1
    return total_words

def Word_frequency(filename):
    dic = collections.Counter()
    with open (filename) as f:
        for line in f:
            for word in line.split():
                dic[word] += 1
    print (dic)
    return dic


#comedy_file=open(comedy_file_name)
#comedy_file.readlines()
print ("There are "+str(Word_count(comedy_file_name))+" words in Shakespeare's Comedy of Errors")
print ("There are "+str(Word_count(tragedy_file_name))+" words in Shakespeare's Anthony and Cleopatra")
Word_frequency(tragedy_file_name)