import os
import re
from nltk.stem import PorterStemmer
from nltk.corpus import words

ps = PorterStemmer()

path = os.getcwd()

training_file = "train_docs.dat"
test_file = "test_docs.dat"
training_dir = path+"/reuters/training"
test_dir = path+"/reuters/test"
num_file = 0
list_train_files = os.listdir(training_dir)
#print(len(list_train_files))
list_test_files = os.listdir(test_dir)
#print(len(list_test_files))

traingfile = open(training_file,"w")
traingfile.write("%d \n"%(len(list_train_files)))


#load Stop word
stop_word = []

with open(path+"/reuters/stopwords") as stw_file:
    for line in stw_file:
        stop_word.append(line.strip())
        #print(line)
#print (stop_word)

#print(list_train_files)

for file_name in list_train_files:
    with open(training_dir+"/"+file_name,"r") as doc_file:
        print(training_dir+"/"+file_name)
        for line in doc_file:
            lst = line.strip().split()
            lst_fl = filter(lambda w: w not in stop_word,lst)
            #lst_fl = filter(lambda w: w in words.words(), lst)
            lst_fl = map(lambda w : ps.stem(re.sub('[^A-Za-z]+', '', w)).lower(),lst_fl)
            line =" ".join(lst_fl)
            traingfile.write(line.strip()+" ")
    traingfile.write("\n")

traingfile.close()

testfile = open(test_file,"w")
testfile.write("%d \n"%len(list_test_files))
for file_name in list_test_files:
    with open(test_dir+"/"+file_name,"r") as doc_file:
        print(test_dir+"/"+file_name)
        for line in doc_file:
            lst = line.strip().split()
            lst_fl = filter(lambda w: w not in stop_word,lst)
            #lst_fl = filter(lambda w: w in words.words(), lst)
            lst_fl = map(lambda w: ps.stem(re.sub('[^A-Za-z]+', '', w)).lower(), lst_fl)
            line =" ".join(lst_fl)
            testfile.write(line.strip()+" ")
    testfile.write("\n")

testfile.close()