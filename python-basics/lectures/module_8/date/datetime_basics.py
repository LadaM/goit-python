from datetime import datetime

d = datetime(year=2002, month=5, day=11, hour=19, minute=23, second=12)
print(d)
print(d.date()) # also works with .time() .year()

print(f"Current time is {datetime.now()}") # date object doesn't have the method now() -> get the date by datetime.now().date()
print(f"Current time from datetime.today() is {datetime.today()}")