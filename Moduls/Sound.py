import pyttsx3
import speech_recognition as sr

engine=pyttsx3.init()

def Listen(IsSleep=False):
    try:
        ear=sr.Recognizer()
        with sr.Microphone() as source:
            if not IsSleep:
                print("Listening.....")
            audio=ear.listen(source,timeout=5,phrase_time_limit=7)
            sentence=ear.recognize_google(audio,language="en")
            return sentence
    except Exception as e:
        if not IsSleep:
            return 1
        else:
            return " "
    

def Speak(text,IsPrint=True):
    if IsPrint:
        print("MINI: ",text)        
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[3].id)
    engine.setProperty("rate",167)
    engine.say(text)
    engine.runAndWait()


if __name__=="__main__":
    Speak(Listen())
    