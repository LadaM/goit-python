# original string
string = "GFG"
# Right Padding of the string
right_padding = ('{:-<7}'.format(string))
print(f'\"{right_padding}\"')
 
# Left Padding of the string
left_padding = ('{: >5}'.format(string))
print(f'\"{left_padding}\"')
 
# Center Padding of the string
central_padding = ('{:-^5}'.format(string))
print(f'\"{central_padding}\"')

# to use programmatically defined padding
padding = 5
print("Hello".rjust(padding))