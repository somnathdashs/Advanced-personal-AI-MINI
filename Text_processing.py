import numpy as np # pip install numpy
import nltk # pip install nltk
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize

# nltk.download("punkt")

Stemmer=PorterStemmer()

def Tokenize(Sentence):
    return word_tokenize(Sentence)

def Stem(word):
    word=str(word) # hello
    return Stemmer.stem(word.lower())


def One_Hot_Encoding(Tokens,Vocab):
    sent=[Stem(word) for word in Tokens]
    bag=np.zeros(len(Vocab),dtype=np.float32)
    for index,word in enumerate(Vocab):
        if word in sent:
            bag[index]=1
    return bag



def Filteration_of_sen(Sentence):
    opporers=["+","-","*","/","<",">","="] # 5 + 5
    Sentence=str(Sentence).lower()
    for o in opporers:
        if o in Sentence:
            Sentence=Sentence.replace(o,f" {o} ")
    return Sentence


    





