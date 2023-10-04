def real_len(text):
    to_remove = ['\n', '\f', '\r', '\t', '\v']
    result = text
    for c in to_remove:
        result = result.replace(c, '')
    
    return len(result)
    
    
print(real_len('Al\nKdfe23\t\v.\r'))
print(real_len('Alex\nKdfe23\t\f\v.\r'))