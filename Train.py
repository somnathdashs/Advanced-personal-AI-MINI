import json
import tensorflow as tf
import numpy as np
import Text_processing as T_process
from tensorflow import keras
import pickle

Data=json.load(open("./Data.json"))
Tags=[]
for i in Data["intents"]:
    Tags.append(i["tag"])

# print(len(Tags))

Tags=sorted(set(Tags))

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


for i,x in enumerate(X):
    X[i]=T_process.One_Hot_Encoding(x,Vocab)

X=np.array(X)
Y=np.array(Y)


def Neural_Network(input_shape,output_shape):
    model=keras.Sequential([
        keras.layers.Dense(256,activation="relu",input_shape=input_shape), #Input Layer
        #Hidden layer
        keras.layers.Dense(128,activation="relu"),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(64,activation="relu"),
        keras.layers.Dense(16,activation="relu"),
        keras.layers.Dropout(0.2),
        #outpu layer
        keras.layers.Dense(output_shape,activation="softmax")
    ])
    model.compile(optimizer="adam",loss=keras.losses.SparseCategoricalCrossentropy(),metrics=["accuracy"])
    return model

MINI=Neural_Network(input_shape=(len(X[0]),) , output_shape=len(Tags))


MINI.fit(X,Y,epochs=150)



MINI_data={
    "Architecture":MINI.to_json(),
    "Weight":MINI.get_weights(),
    "Vocab":Vocab,
    "Tags":Tags
}

pickle.dump(MINI_data,open("./MINI.pkl","wb"))