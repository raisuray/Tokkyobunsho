from spacy.matcher import Matcher
import spacy

def load_matcher():
    nlp = spacy.load("ja_ginza")

    matcher_temp = Matcher(nlp.vocab)

    conclusion = [
        {'OP':'*'}, {'TEXT':'よう', 'POS':'AUX'}, {'TEXT':'に', 'POS':{'IN':['AUX', 'ADP']}}
    ]

    method1 = [
        {'OP':'*'}, {'TEXT':'だけ', 'POS':'ADP'}, {'TEXT':'で', 'POS':{'IN':['AUX', 'ADP']}}
    ]

    method2 = [
        {'OP':'*'}, {'TEXT':'で', 'POS':{'IN':['AUX', 'ADP']}}, {'TEXT':'は', 'POS':{'IN':['AUX', 'ADP']}}
    ]

    method3 = [
        {'OP':'*'}, {'TEXT':'に', 'POS':{'IN':['AUX', 'ADP']}}, {'LEMMA':'よる', 'POS':'VERB'}
    ]
    method4 = [
        {'OP':'*'}, {'TEXT':'に', 'POS':{'IN':['AUX', 'ADP']}}, {'LEMMA':'よる', 'POS':'VERB'}
    ]
    method5 = [
        {'OP':'*'}, {'TEXT':'に', 'POS':{'IN':['AUX', 'ADP']}}, {'TEXT':'よれ', 'POS':'VERB'}, {'TEXT':'ば', 'POS':'SCONJ'}
    ]

    matcher_temp.add('conclusion', None, conclusion)
    matcher_temp.add('method1', None, method1)
    matcher_temp.add('method2', None, method2)
    matcher_temp.add('method3', None, method3)
    


    return matcher_temp