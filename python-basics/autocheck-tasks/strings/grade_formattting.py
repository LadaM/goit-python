grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    formatted_lines = []
    line_nr = 1
    for name, grade in students.items():
        formatted_lines.append("{:>4}|{:<10}|{:^5}|{:^5}".format(line_nr, name, grade, grades.get(grade)))
        line_nr += 1
    return formatted_lines

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
lines = formatted_grades(students)
for line in lines:
    print(line)