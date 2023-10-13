from datetime import datetime, date

# date formatted as '2020-10-09'
def get_days_from_today(date):
    parsed_date = datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.today()
    difference = current_date - parsed_date
    return difference.days

if __name__ == "__main__":
    print(get_days_from_today("2021-05-05"))
    print(date(year=2021, month=5, day=5) - date(year=2023, month=10, day=9))