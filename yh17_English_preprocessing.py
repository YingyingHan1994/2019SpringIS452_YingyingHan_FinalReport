infile=open("EnglishVer_BookI.txt","r",encoding ='utf-8')
allthelines =infile.read()
#print(allthelines)
infile.close()


############# Now, I am going to remove all the header and footer####################

startpoint =allthelines.find("CHAPTER I.")
#print(startpoint)
endpoint = allthelines.find("END OF BOOK I")
#print(endpoint)
chapters = allthelines[startpoint:endpoint]
#print(chapters)

############Now, I am going to lowercase all the word#################
lower_chapters = chapters.lower()
#print(lower_chapters)


#############Now, I am going to remove all the punctuations####################
import string
#print(string.punctuation)
for punc in string.punctuation:
    lower_chapters = lower_chapters.replace(punc,"")
#print(lower_chapters)


#############Now, I am going to remove all the numbers##########################
def removeNumberFromStrings(string):
    newString =""
    for ch in string:
        if ch =="0" or ch =="1" or ch =="2" or ch=="3" or ch=="4" or ch=="5" or ch=="6" or ch=="7" or ch=="8" or ch=="9":
             newString = newString
        else:
             newString = newString + ch
    return newString

number_removed_chapters = removeNumberFromStrings(lower_chapters)
#print(number_removed_chapters)



###############Now, I am going to remove the leading and trailing white spaces#########################
number_removed_whitespaces_removed_chapters =number_removed_chapters.strip()
#print(number_removed_whitespaces_removed_chapters)


###############Now, I want to explore the data: count the number of times each word appears#############
listversion =number_removed_whitespaces_removed_chapters.split()

counts=dict()
for word in listversion:
    if word not in counts:
        counts [word] =1
    else:
        counts [word] +=1
items =list(counts.items())
#print(items)

for pairs in items:
    key = pairs[0]
    value =pairs [1]
    #print(key)
    #print (value)

def byFreq (pair):
    return pair[1]

items.sort(key = byFreq, reverse=True)
#print(items[0:200])


################Now, I am going to remove the stopwords from the text file############################
################I use the stop words list on the Moodle page##########################################
infile = open("stopwords.txt","r")
stopwords = infile.readlines()
infile.close()
#print(stopwords)
new_stopwords=[]
for each_stopword in stopwords:
    new_stopwords.append(each_stopword.strip())
#print(new_stopwords)

without_stopwords = []
for words in listversion:
    if words not in new_stopwords:
        without_stopwords.append(words)
#print(without_stopwords)

counts=dict()
for word in without_stopwords:
    if word not in counts:
        counts [word] =1
    else:
        counts [word] +=1
items =list(counts.items())
#print(items)

for pairs in items:
    key = pairs[0]
    value =pairs [1]
    #print(key)
    #print (value)

def byFreq (pair):
    return pair[1]

items.sort(key = byFreq, reverse=True)
#print(items[0:200])











