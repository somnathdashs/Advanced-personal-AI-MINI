from datetime import datetime,date,timedelta
import pywhatkit

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

    return response_given