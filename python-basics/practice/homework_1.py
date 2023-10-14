from datetime import datetime, date
from collections import defaultdict

# >>>> TASK 1 <<<<
data = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Orlando Bloom", "birthday": datetime(1987, 10, 27)},
    {"name": "Matthew Harris", "birthday": datetime(1960, 7, 10)},
    {"name": "Matt Johnes", "birthday": datetime(1991, 1, 10)},
    {"name": "Nathalie Portman", "birthday": datetime(1967, 11, 1)},
]

def get_birthday_per_week(data):
    name_by_weekday = defaultdict(list)
    # today = datetime.now().date()
    for d in data:
        dt = d["birthday"]
        weekday = dt.strftime("%A")
        name_by_weekday[weekday].append(d["name"])
    return name_by_weekday

print(get_birthday_per_week(data))

def comparator(element):
    return element["birthday"]
data.sort(key=comparator)
print(data)

# >>>> TASK 2 <<<<
contacts = [
    {"Ivan Ivanovic": "32690869246"},
    {"Nobody You Know": "79-784765-12"},
    {"Someone Else": "66-978-44-12"},
    {"Peter Smith": "77-78-779-77"},
]

name = "Ivan Ivanovic"
# update phone number
for contact in contacts:
    if name in contact:
        contact[name] = "new phone number"