from datetime import datetime

def weekday(date: str):
    d = datetime.strptime(date, "%d-%m-%Y")
    day = d.strftime("%A") # -> for month use %B
    print(day)
    pass

weekday("31-05-2004")