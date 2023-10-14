from datetime import datetime,date,timedelta

def Task(response_given):
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

    return response_given