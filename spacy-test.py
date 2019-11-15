import spacy
import pandas as pb
import random as rd
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

df = (pb.read_csv("data/Questions.csv",encoding="ISO-8859-1",nrows=1_000_000,usecols=['Title','Id']))

titles = [_ for _ in df['Title']]

rd.choices(titles,k=20)

def has_golang(text):
    return " go " in text

g = (title for title in titles if has_golang(title))
print([next(g) for i in range(5)])

doc = nlp ("My name is Ganga Tamang")
displacy.render(doc)


