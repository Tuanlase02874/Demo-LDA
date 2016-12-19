import os
from nltk.corpus import words

path = os.getcwd()
file_out = open("wordmap_clean.txt","w")
map_word = []
with open(path+"/wordmap.txt","r") as stw_file:
    for line in stw_file:
        ls = line.strip().split()[0]
        if ls in words.words():
            file_out.write(line)
            print(line)

file_out.close()