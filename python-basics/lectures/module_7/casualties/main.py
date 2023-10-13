import calendar
from pathlib import Path
from constants import MENU, FILENAME
from exceptions import NotInRange
from faker import Faker

path_to_file = Path.joinpath(Path(__file__).parent, FILENAME)
print(path_to_file)
def add_new_record(name, amount):
    with open(path_to_file, 'a') as file:
        fake = Faker()
        current_date = fake.date_between("-1y").strftime("%m/%d/%y")
        print(current_date)
        record = f"{current_date: > 15}{name: ^40}"
    pass

def show_statistics():
    pass

def show_statistics_for_month():
    pass

def show_calendar_for_year(year: int):
    print(calendar.calendar(year))

while True:
    print(MENU)
    try:
        choice = int(input("Make your choice please >>> "))
        if choice < 1 or choice > 5:
            raise NotInRange
    except ValueError:
        print("Please choose the number from the menu")
        continue
    except NotInRange:
        print("Choose option from 1 - 5")
        continue

    if choice == 1:
        print("Please enter data in the following format: <name>:<amount>")
        try:
            s = input(">>> ")
            name, count = s.split(":")
            add_new_record(name, count)
        except:
            print("Cannot parse the data you've entered. Please try again.")
            continue
    elif choice == 2:
        show_statistics()
    elif choice == 3:
        print("Please enter a year")
        try:
            year = int(input(">>> "))
        except ValueError:
            print("Please enter a valid year")
            continue
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print("You did great today. See you soon!")
        break # to break out of the loop