import re

def is_integer(s):
    
    if len(s) == 0:
        return False
    
    match = re.match('^[+-]?[0-9]+$', s.strip())    
    
    return bool(match)

is_integer(' -34')