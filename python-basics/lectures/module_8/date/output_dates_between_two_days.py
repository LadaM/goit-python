from datetime import datetime, date, timedelta

start_date = date(year=2023, day=12, month=10)
end_date = date(year=2023, day=31, month=10)

days = (end_date - start_date).days # -> timedelta
print(f"{days} between {start_date} and {end_date}")

for i in range(days):
    res = start_date + timedelta(days=i)
    print(res.strftime("%Y-%m-%d"))