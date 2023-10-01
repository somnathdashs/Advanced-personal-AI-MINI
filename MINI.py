import json
import numpy as np
import tensorflow as tf
import pickle,random
import Text_processing as T_Process

Dataset=json.load(open("./Data.json","r"))
MINI_data=pickle.load(open("./MINI.pkl","rb"))
Vocab=MINI_data["Vocab"]

def Text_processing(text):
    sentence=T_Process.Tokenize(T_Process.Filteration_of_sen(text))
    sentence=T_Process.One_Hot_Encoding(sentence,Vocab)
    return sentence.reshape(1,sentence.shape[0])

def Nrandom(intend,text):
    pass

MINI=tf.keras.models.model_from_json(MINI_data["Architecture"])
MINI.set_weights(MINI_data["Weight"])
Tags=MINI_data["Tags"]

while True:
    User_input=input("Enter your command >>")
    User_input=Text_processing(User_input)
    answer=MINI.predict(User_input)
    index=np.argmax(answer)
    tag=Tags[index]
    acc=int(answer[0][index]*100)
    if acc >60:
        for intent in Dataset["intents"]:
            if tag== intent["tag"]:
                if "nrandom" in intent["responses"]:
                    pass
                else:
                    response=random.choice(intent["responses"])
        
        print(response, acc)





