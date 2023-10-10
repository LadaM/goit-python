def formatted_numbers():
    ''' Outputs table of numbers 0..15 as decimal, hex, and binary.
    '''
    formatted_strings = []
    header = "{:^10}|{:^10}|{:^10}".format('decimal', 'hex', 'binary')
    formatted_strings.append(header)
    for num in range(16):
        formatted_strings.append(
            "{:<10d}|{:^10x}|{:>10b}".format(num, num, num)
        )
    return formatted_strings

for s in formatted_numbers():
    print(s)