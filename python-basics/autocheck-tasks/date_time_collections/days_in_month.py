from datetime import date

def get_days_in_month(month, year):
    next_month = date(year=year, month=month + 1, day=1) if month <  12 else date(year=year+1, month=1, day=1)
    return(next_month - date(year=year, month=month, day=1)).days

if __name__ == "__main__":
    print(get_days_in_month(2, 2024))