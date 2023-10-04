def get_grade(key):
    grade_by_ects_scale = {
        'A':5,
        'B':5,
        'C':4,
        'D':3,
        'E':3,
        'FX':2,
        'F':1
    }
    return grade_by_ects_scale.get(key)
    


def get_description(key):
     description_by_ects_scale = {
        'A':'Perfectly',
        'B':'Very good',
        'C':'Good',
        'D':'Satisfactorily',
        'E':'Enough',
        'FX':'Unsatisfactorily',
        'F':'Unsatisfactorily'
    }
     return description_by_ects_scale.get(key)

print(
     get_grade('A'),
     get_grade('B'),
     get_grade('C'),
     get_grade('D'),
     get_description('FX'),
     get_description('F'),
     get_description('M')
)