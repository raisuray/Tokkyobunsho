
from spacy import matcher
from patent import PatentH
import os
import spacy
import tools
import json 
import pprint
from spacy import displacy
from pathlib import Path
from spacy.matcher import Matcher
import re
import neologdn
from matcher import load_matcher

path = './effect_words/'
effect_words = os.listdir(path)
dict_eff_words = dict.fromkeys(effect_words)


patents_list = []

for patent in dict_eff_words.keys():
    file_path = path+patent
    new = PatentH(file_path)
    patents_list.append(new)

#print(patents_list[0].doc)


text_temp = patents_list[0].doc
text = ''
for i in range(len(text_temp)):
    text_temp[i] = neologdn.normalize(text_temp[i])
    text += text_temp[i]

#print(text)
#text = text.split("\n")
#text = text.split("。")

nlp = spacy.load("ja_ginza")
"""
matcher = Matcher(nlp.vocab)

conclusion = [
    {'OP':'*'}, {'TEXT':'よう', 'POS':'AUX'}, {'TEXT':'に', 'POS':'AUX'}
]

method = [
    {'OP':'*'}, {'TEXT':'だけ', 'POS':'ADP'}, {'TEXT':'で', 'POS':'AUX'}
]


matcher.add('conclusion', None, conclusion)
matcher.add('method', None, method)
"""


text = neologdn.normalize("本発明によると、チタンとアルミニウムの金属間化合物Ｔｉ3 Ａｌの単体を高純度でしかも、多量生産で安価に粉末状または塊状で得られる。本発明による金属間化合物Ｔｉ3 Ａｌの単体粉末を粉末冶金法に適用することによって、切削溶接加工が少なくて済む製品形状に近い大型焼結体を形成し、各種装置として構造物に直接組み込める。また焼結体は、スパッタリングや真空蒸着のターゲット材料にも使用でき、各種の構造物の表面処理を行い、耐熱性を高め、機械強度を向上させることができる。本発明による金属間化合物Ｔｉ3 Ａｌを組み込んだ各種製品は軽量で優れた熱性、耐食性、高い機械強度を有しており、製造価格が安い。金属間化合物Ｔｉ3 Ａｌを組み込んだ各種製品、たとえば、航空機や宇宙船関連機器や深海艇など海洋関連機器や磁気浮上列車などの交通関連機器等を構成する機械構造製品、ジェットエンジンや自動車用エンジンや発電機用タービン等に使われるタービンブレード等高温利用動力発生装置等に使用され、本発明はこれらを安価に提供できる工業上大いなる利益がある。")
print(text)
matcher = load_matcher()

doc = nlp(text)
for span in doc.sents:
    total = 0
    for m , s , e in matcher(span):
        print(m)
        print(span[s:e])
       