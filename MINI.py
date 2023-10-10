import json
import numpy as np
import tensorflow as tf
import pickle,random
import Text_processing as T_Process
from NRandom import FSCosine
from Moduls.Sound import Speak,Listen

Dataset=json.load(open("./Data.json","r"))
MINI_data=pickle.load(open("./MINI.pkl","rb"))
Vocab=MINI_data["Vocab"]

def Text_processing(text):
    sentence=T_Process.Tokenize(T_Process.Filteration_of_sen(text))
    sentence=T_Process.One_Hot_Encoding(sentence,Vocab)
    return sentence.reshape(1,sentence.shape[0])

def Nrandom(intend,text):
    index=FSCosine().Find_similarity(intend,text)+1
    return index

MINI=tf.keras.models.model_from_json(MINI_data["Architecture"])
MINI.set_weights(MINI_data["Weight"])
Tags=MINI_data["Tags"]

while True:
    User_input_str=Listen()
    User_input=Text_processing(User_input_str)
    answer=MINI.predict(User_input)
    index=np.argmax(answer)
    tag=Tags[index]
    acc=int(answer[0][index]*100)
    if acc >60:
        for intent in Dataset["intents"]:
            if tag== intent["tag"]:
                if "nrandom" in intent["responses"]:
                    i=Nrandom(intent["patterns"],User_input_str)
                    response=random.choice(intent["responses"][i])
                else:
                    response=random.choice(intent["responses"])
        
        Speak(response)





