applicants = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

def format_applicants():
    result = []
    for a in applicants:
        name, specialty, math, lang, eng = a.values()
        a_string = f"{name}, {specialty}, {math}, {lang}, {eng}"
        # a_string = f"{a.get('name')}, {a.get('specialty')}, {a.get('math')}, {a.get('lang')}, {a.get('eng')}"
        result.append(a_string)
    print('\n'.join(result))
    
format_applicants()