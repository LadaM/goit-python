ALPHABET_COUNT = 26
a_POS = ord('a')
A_POS = ord('A')
message = input("Enter a message: ")
offset = int(input("Enter the offset: "))

encoded_message = ""
for ch in message:
    if ch.isalpha():
        start_pos = A_POS if ch.isupper() else a_POS
        pos = ord(ch) - start_pos
        pos = (pos + offset) % ALPHABET_COUNT
        shifted_char = chr(pos + start_pos)
        encoded_message += shifted_char
    else:
        encoded_message += ch

print(encoded_message)