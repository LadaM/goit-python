from datetime import datetime, date

# ISO '2021-05-27 17:08:34.149Z' -> 'Thursday 27 May 2021'
def get_str_date(date):
    iso_date = datetime.fromisoformat(date)
    return datetime.strftime(iso_date, "%A %d %B %Y")

if __name__ == "__main__":
    print(get_str_date('2021-05-27 17:08:34.149Z')) 