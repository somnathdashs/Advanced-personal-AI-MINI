from datetime import datetime,date,timedelta
import pywhatkit
import wolframalpha # pip install wolframalpha
import wikipedia
from Moduls import Personal

Wolfarm_app=wolframalpha.Client(Personal.WolfarnID)


def Task(response_given,UserInput_str):
    response=str(response_given).lower()
    if "time" in response:
        return datetime.now().strftime("%I:%M %p")
    
    elif "ydate" in response:
        Ydate=date.today()-timedelta(days=1)
        return Ydate.strftime("%d %B %Y")

    elif "tdate" in response:
        Tdate=date.today()+timedelta(days=1)
        return Tdate.strftime("%d %B %Y")

    elif "date" in response:
        return datetime.now().strftime("%d %B %Y")
    
    elif "music" in response:
        pywhatkit.playonyt(UserInput_str)
        return "Playing your song"
    
    elif "math" in response or "squestions" in response:
        try:
            return Wolfarm_Alpha(UserInput_str)
        except:
            ignore_word=["wiki","wikipedia","search","tell","about","me","something"]
            for i in ignore_word:
                UserInput_str=UserInput_str.replace(i,"")
            return Wiki(UserInput_str)

    return response_given

















def Wolfarm_Alpha(quary):
    response=Wolfarm_app.query(quary)
    response=(next(response.results)).text
    return response

def Wiki(quary):
    try:
        return wikipedia.summary(quary,2)
    except:
        return "Having some problem while fetching data."





