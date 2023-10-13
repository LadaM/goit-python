from datetime import datetime

# Python strftime() Method
# %Y - year [0001,..., 2018, 2019,..., 9999]
# %m - month [01, 02, ..., 11, 12]
# %d - day [01, 02, ..., 30, 31]
# %H - hour [00, 01, ..., 22, 23.
# %M - minute [00, 01, ..., 58, 59]
# %S - second [00, 01, ..., 58, 59]

# if user input is 
input_date = '12.10.23'
parsed_date = datetime.strptime(input_date, "%d.%m.%y")
print(parsed_date)


# date --> string
formatted_date = parsed_date.strftime("%y/%d/%m %H:%M")
print(formatted_date)

# to change something inside a date use .replace
changed_date = parsed_date.replace(year=2000)
print(f"Changed datetime {changed_date}, initial datetime {parsed_date}")

# can substract dates (no adding is possible)
delta = parsed_date - changed_date
print(delta)