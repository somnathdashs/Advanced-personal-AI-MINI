import json
import tensorflow as tf
import numpy as np
import Text_processing as T_process

Data=json.load(open("./Data.json"))
Tags=[]
for i in Data["intents"]:
    Tags.append(i["tag"])

# print(len(Tags))


X,Y=[],[]
Vocab=[]

for data in Data["intents"]:
    for question in data["patterns"]:
        if type(question)==list:
            for i in question:
                sentence=T_process.Tokenize(T_process.Filteration_of_sen(i))
                Vocab.extend(sentence)
                X.append(sentence)
                Y.append(Tags.index(data["tag"]))
        else:
            sentence=T_process.Tokenize(T_process.Filteration_of_sen(question))
            Vocab.extend(sentence)
            X.append(sentence)
            Y.append(Tags.index(data["tag"]))




ignore_symbole=[",","?","/",".","!","|"]
Vocab=[T_process.Stem(w) for w in Vocab if w not in ignore_symbole]

Vocab=sorted(set(Vocab))
Tags=sorted(set(Tags))


for i,x in enumerate(X):
    X[i]=T_process.One_Hot_Encoding(x,Vocab)

X=np.array(X)
Y=np.array(Y)

print(X.shape,Y.shape)
print(X[0])

