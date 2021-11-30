"""
Main Program
"""    

from patent import Patent
import os
import spacy
import tools
import json 


path = './effect_words/'
effect_words = os.listdir(path)
dict_eff_words = dict.fromkeys(effect_words, [])


patents_list = []

for patent in dict_eff_words.keys():
    file_path = path+patent
    new = Patent(file_path)
    patents_list.append(new)

#FIND ALL THE COMPOUND WORD IN ALL FILE#
nlp = spacy.load("ja_ginza")
for patent in patents_list:
    print(patent.name)

    for i in range(len(patent.doc)):
        doc_samp = nlp(patent.doc[i])
        list_of_compound_word = tools.find_noun_and_compound(doc_samp, i)
    
    dict_eff_words[patent.name].extend(list_of_compound_word)

#MAKE AN OUTPUT FILE#
with open("out.json", 'w') as f:
        json.dump(dict_eff_words,f, indent=4, ensure_ascii=False)

