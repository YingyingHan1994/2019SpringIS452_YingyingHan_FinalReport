# -*- coding: UTF-8 -*-
infile=open('ChineseVer_UTF8.txt',"r",encoding='utf-8')
allthechineselines=infile.read()
infile.close()
#print(allthechineselines)


###########################Now, I am going to extract the first 24 chapters out###########################
startpoint = allthechineselines.find("第一回")
#print(startpoint)
endpoint = allthechineselines.find("第二十五回")
chapters=allthechineselines[startpoint:endpoint]
#print(chapters)

###########################Now, I am going to remove the whitespaces#########################################
chapter_without_whitespaces=chapters.strip()
#print(chapter_without_whitespaces)

#########################Chinese word segementation############################################################
import jieba
seg_list = jieba.cut(chapter_without_whitespaces)
#print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#print(type(seg_list))

#################Now, I am going to remove the stopwords from the text file###################################

infile = open("Chinese_Stopwords.txt","r",encoding="utf-8")
chinesestopwords = infile.readlines()
infile.close()
#print(chinesestopwords)

new_chinese_stopwords=[]
for each_stopword in chinesestopwords:
    new_chinese_stopwords.append(each_stopword.strip())
#print(new_chinese_stopwords)

without_stopwords_chinese = []
for words in seg_list:
     if words not in new_chinese_stopwords:
         without_stopwords_chinese.append(words)
#print(without_stopwords_chinese)

counts=dict()
for word in without_stopwords_chinese:
     if word not in counts:
         counts [word] =1
     else:
         counts [word] +=1
items =list(counts.items())
#print(items)

for pairs in items:
     key = pairs[0]
     value =pairs [1]


def byFreq (pair):
     return pair[1]

items.sort(key = byFreq, reverse=True)
#print(items[0:400])


###############Now, I am going to split the text by period##############################################
chinesetext=""
for eachword in without_stopwords_chinese:
    chinesetext=chinesetext+eachword
#print(chinesetext)

sentences=chinesetext.split("。")
#print(sentences)

##############Now, I want to see how many time Pao-yu smile#########################################
chinese_paoyu_smile_sentences =[]
for each_sentence in sentences:
    if "寶玉" in each_sentence and "笑" in each_sentence:
        chinese_paoyu_smile_sentences.append(each_sentence)
print(len(chinese_paoyu_smile_sentences))

##############Now, I want to see how many time tai-yu smile#########################################
chinese_taiyu_smile_sentences =[]
for each_sentence in sentences:
    if "黛玉" in each_sentence and "笑" in each_sentence:
        chinese_taiyu_smile_sentences.append(each_sentence)
print(len(chinese_taiyu_smile_sentences))

##############Now, I want to see how many time baichia smile#########################################
chinese_paochia_smile_sentences =[]
for each_sentence in sentences:
    if "寶釵" in each_sentence and "笑" in each_sentence:
        chinese_paochia_smile_sentences.append(each_sentence)
print(len(chinese_paochia_smile_sentences))


import csv

paoyu_smile_result = [chinese_paoyu_smile_sentences]

with open('chinese_paoyu_smile_result.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(paoyu_smile_result)

csvFile.close()

taiyu_smile_result =[chinese_taiyu_smile_sentences]
with open('chinese_taiyu_smile_result.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(taiyu_smile_result)

csvFile.close()

paochi_smile_result =[chinese_paochia_smile_sentences]
with open('chinese_paochia_smile_result.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(paochi_smile_result)

csvFile.close()
