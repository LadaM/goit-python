import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

#  [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
def convert_list(cats):
    ''' Converts list of namedtuples to list of dictionaries and vica versa
    '''
    converted_list = []
    for cat in cats:
        if isinstance(cat, dict):
            converted_list.append(Cat(**cat))
        else:
            converted_list.append(cat._asdict())
            # cats_dicts.append({"nickname": cat.nickname, "age": cat.age, "owner": cat.owner})
    return converted_list
        
            
convert_list([Cat(nickname='Mick', age=5, owner='Sara'), Cat(nickname='Barsik', age=7, owner='Olga'), Cat(nickname='Simon', age=3, owner='Yura')])               
            
        
    
        
    