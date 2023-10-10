import re

def capital_text(s: str):
    words = s.split()
    capitalize_next = False

    for i, w in enumerate(words):
        if i == 0 or capitalize_next:
            words[i] = w.capitalize()
        # re.match() doesn't give the same result in this case as re.search()
        capitalize_next = bool(re.search('[.,?!]', w))
        
    return ' '.join(words)
    
print(capital_text('dummies!!!! fools! I am done with you...'))