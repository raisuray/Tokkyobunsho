import spacy as spacy
import sys

nlp = spacy.load("ja_ginza")

while True:
    text = input("put your word : ")
    if(len(text) <= 0):
        sys.exit()
    doc = nlp(text)

    for token in doc:
        print(token.text, token.pos_)
    

