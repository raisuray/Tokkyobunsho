import spacy
import re
import neologdn
import json
import pprint


from IGNORE_WORDS import ig

def find_noun_and_compound(doc, i):
    
    found_compound_noun = 0
    count = 0
    compound = ''
    maxword = len(doc)

    list_of_compound_word = set()
    """
    list_of_noun_word = set()
    list_all_words = set()
    """

    while True:
        
        
        try:    
            if(doc[count].pos_ == "NUM" and doc[count+1].dep_ == "compound"):
                compound += doc[count].text
                count += 1
        except IndexError:
            #print("Index out of limit! Line : " + str(i) + " 気にしないで")
            pass
    
        
        norm = neologdn.normalize(doc[count].norm_).isascii 
        while doc[count].dep_ == "compound" and doc[count].pos_ == "NOUN" and (norm != True):
            text = doc[count].text
            if (text in ig):
                break
            compound += text
            count += 1
            found_compound_noun = 1
        
        if(found_compound_noun == 1 and doc[count].pos_ == "NOUN"):
            if(doc[count].text in ig ):
                compound = ''
                found_compound_noun = 0                
            else :
                compound += doc[count].text
                found_compound_noun = 0
                list_of_compound_word.add(compound)
                #print(compound)
                compound = ""
       
        else:
            compound = ''
            found_compound_noun = 0
        
        """
        if(doc[count].pos_ == "NOUN" and found_compound_noun != 1):
            if(doc[count].text not in ig):
                list_of_noun_word.add(doc[count].text)
        """
        count += 1

        if(count == maxword):
            break
        
        
    """
    for word in list_of_compound_word:
        list_all_words.add(word)

    for word in list_of_noun_word:
        list_all_words.add(word)
    """

    list_of_compound_word = list(list_of_compound_word)

    """
    list_of_noun_word = list(list_of_noun_word)
    list_all_words = list(list_all_words)
    """

    return list_of_compound_word

def exct_experimental_section(doc):

    start   = 0
    end     = 0
    read    = 0
    pattern_start = re.compile("【実施例.*】|（実施例.*）")
    pattern_end  = re.compile("【発明.*】|（発明.*）|【図面の簡単な.*】")

    exp_texts = []

    for i, experiment in enumerate(doc):
        if(read == 0 and pattern_start.match(experiment) != None):   
            read = 1
            start = i
        if(read == 1 and pattern_end.match(experiment) != None):
            end = i
            break

    exp_texts = doc[start:end]

    for i in range(len(exp_texts)):
        exp_texts[i] = re.sub(r"【.*】|（.*） ?|〔[１２３４５６７８９０]?〕|<.*>|〈.*〉", "", exp_texts[i])
        exp_texts[i] = re.sub("\n| ?", "",exp_texts[i])
        exp_texts[i] = neologdn.normalize(exp_texts[i])

    while "" in exp_texts:
        exp_texts.remove("")

    #pprint.pprint(exp_texts)
    return exp_texts

def exct_hatsumei_section(doc):

    start   = 0
    end     = 0
    read    = 0
    pattern_start = re.compile("【発明の効果】|（発明の効果）")
    pattern_end  = re.compile("【図面の簡単な.*】")

    exp_texts = []

    for i, experiment in enumerate(doc):
        if(read == 0 and pattern_start.match(experiment) != None):   
            read = 1
            start = i
        if(read == 1 and pattern_end.match(experiment) != None):
            end = i
            break

    exp_texts = doc[start:end]

    for i in range(len(exp_texts)):
        exp_texts[i] = re.sub(r"【.*】|（.*） ?|〔[１２３４５６７８９０]?〕|<.*>|〈.*〉", "", exp_texts[i])
        exp_texts[i] = re.sub("\n| ?", "",exp_texts[i])
        exp_texts[i] = neologdn.normalize(exp_texts[i])

    while "" in exp_texts:
        exp_texts.remove("")

    #pprint.pprint(exp_texts)
    return exp_texts

    


def make_one(out):
    #out["list_all_words"] = list(set( out["list_all_words"]))
    out["list_of_compound_word"] = list(set(out["list_of_compound_word"]))
    #out["list_of_noun_word"] = list(set(out["list_of_noun_word"]))
    return out

def check_symbol(doc):
    for i in doc:
        pos = i.pos_
        if (pos == "SYM"):
            return True
    return False
    

def load_jsonfile(path):
    with open(path, "r") as f:
        x = json.load(f)
    return x

def save_jsonfile(path, value):
    with open(path, 'w') as f:
        json.dump(value, f, indent=4, ensure_ascii=False)



if __name__ == '__main__':
    
    nlp = spacy.load("ja_ginza")
    

    file_name = '1992172658.txt'

    out = {'list_of_compound_word':[]}
    
    with open('effect_words/'+file_name ,mode='r') as f:
        doc = f.readlines()

    doc = exct_experimental_section(doc)
    pprint.pprint(doc)
    for i in range(len(doc)):
        doc_samp = nlp(doc[i])
        if(check_symbol(doc_samp)==True and len(doc[i]) <= 10):
            continue

        list_of_compound_word = find_noun_and_compound(doc_samp, i)
        #out["list_all_words"].extend(list_all_words)
        out["list_of_compound_word"].extend(list_of_compound_word)
        #out["list_of_noun_word"].extend(list_of_noun_word)
    out = make_one(out)
    out_final = {file_name:out}
    with open("out2.json", 'w') as f:
        json.dump(out_final,f, indent=4, ensure_ascii=False)
    


   