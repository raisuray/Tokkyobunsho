import json 
import tools
from gensim.models import KeyedVectors

wv = KeyedVectors.load('./patent_w2v_iter5.model') #学習済みモデル(wmDistance)
print("LOAD SUCCESS")

#LOAD 発明効果 FILE
hatsumei = tools.load_jsonfile("./result_02.json")
key_hatsu = hatsumei.keys()

#LOAD 実施例文 FILE
expermnt = tools.load_jsonfile("./out-compound.json")
key_exp = expermnt.keys()


#FIND DISTANCE#
out = dict.fromkeys(key_hatsu)
for textfile in key_hatsu:
    print(textfile)
    l1 = hatsumei[textfile][0]["発明の効果"]
    l2 = expermnt[textfile]
    res = []

    for word in l2:
        for word2 in l1:
            distance = wv.wmdistance(word,word2)
            tup_res = (word, word2, distance)
            res.append(tup_res)
    out[textfile] = res

    out[textfile] = sorted(out[textfile], key=lambda x: x[2])



tools.save_jsonfile("distance.json", out)