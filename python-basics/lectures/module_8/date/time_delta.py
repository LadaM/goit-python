from datetime import datetime, timedelta

current_time = datetime.now()
interval = timedelta(days=2) 

# interval can be added or substracted from a given date
moved_two_days_forward = current_time + interval
print(f"Current time + 2 days is {moved_two_days_forward}")