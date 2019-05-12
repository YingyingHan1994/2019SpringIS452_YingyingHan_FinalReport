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

###############Now, I am going to remove the leading and trailing white spaces#########################
number_removed_whitespaces_removed_chapters =number_removed_chapters.strip()
#print(number_removed_whitespaces_removed_chapters)


###############Now, I am going to split the text by comma##############################################
sentences =number_removed_whitespaces_removed_chapters.split(",")
#print(sentences)


smile_sentences =[]
for each_sentence in sentences:
    if "smil" in each_sentence:
        smile_sentences.append(each_sentence)
#print(smile_sentences)
#print(len(smile_sentences))

###############Now, I want to see how many time Pao-yu smile#########################################
paoyu_smile_sentences =[]
for each_smile_sentence in smile_sentences:
    if "pao-yü smil" in each_smile_sentence:
        paoyu_smile_sentences.append(each_smile_sentence)
#print(len(paoyu_smile_sentences))


#############Now, I want to see how many time tai-yü smil smile######################################
taiyu_smile_sentence =[]
for each_smile_sentence in smile_sentences:
    if "tai-yü smil" in each_smile_sentence:
        taiyu_smile_sentence.append(each_smile_sentence)
#print(len(taiyu_smile_sentence))

###########Now, I want to see how many time paochia smiles############################################################
paochi_smile_sentence =[]
for each_smile_sentence in smile_sentences:
    if "pao chi smile" in each_smile_sentence:
        paochi_smile_sentence.append(each_smile_sentence)
#print(len(paochi_smile_sentence))

##########Now I am going to split the sentence with period instead of comma############################
big_sentences= number_removed_whitespaces_removed_chapters.split(".")
# print(big_sentences)
# print(len(big_sentences))

#########Now, I am going to see how many time the three characters smile################################
paoyu_smile_sentences_2=[]
for each_big_sentence in big_sentences:
    if "pao-yü" in each_big_sentence and "smil" in each_big_sentence:
        paoyu_smile_sentences_2.append(each_big_sentence)
    elif "pao yü" in each_big_sentence and "smil" in each_big_sentence:
        paoyu_smile_sentences_2.append(each_big_sentence)
print(len(paoyu_smile_sentences_2))

taiyu_smile_sentence_2 = []
for each_big_sentence in big_sentences:
    if "tai-yü" in each_big_sentence and "smil" in each_big_sentence:
        taiyu_smile_sentence_2.append(each_big_sentence)
# print(taiyu_smile_sentence_2)
print(len(taiyu_smile_sentence_2))

paochi_smile_sentence_2 =[]
for each_big_sentence in big_sentences:
    if "pao chien" in each_big_sentence and "smil" in each_big_sentence:
        paochi_smile_sentence_2.append(each_big_sentence)
    elif "pao-ch" in each_big_sentence and "smil" in each_big_sentence:
        paochi_smile_sentence_2.append(each_big_sentence)
    elif "lady chai" in each_big_sentence and "smil" in each_big_sentence:
        paochi_smile_sentence_2.append(each_big_sentence)


#print(paochi_smile_sentence_2)
print(len(paochi_smile_sentence_2))

import csv

paoyu_smile_result = [paoyu_smile_sentences_2]

with open('paoyu_smile_result.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(paoyu_smile_result)

csvFile.close()

taiyu_smile_result =[taiyu_smile_sentence_2]
with open('taiyu_smile_result.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(taiyu_smile_result)

csvFile.close()

paochi_smile_result =[paochi_smile_sentence_2]
with open('paochia_smile_result.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(paochi_smile_result)

csvFile.close()




