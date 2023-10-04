def split_list(grade):
    lower_grades = []
    higher_grades = []

    if not grade:
        return (lower_grades, higher_grades)
    
    sum = 0
    for g in grade:
        sum += g
    mean = sum / len(grade)

    grades = sorted(grade)
    for g in grades:
        if g <= mean:
            lower_grades.append(g)
        else:
            higher_grades.append(g)

    return (lower_grades, higher_grades)

print(split_list([3, 28, 41]))