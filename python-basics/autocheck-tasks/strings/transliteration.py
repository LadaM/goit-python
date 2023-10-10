CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
    
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def translate(name):
    return name.translate(TRANS)


print("чаша".translate(TRANS))  # chasha
print("ЧАША".translate(TRANS))  # CHASHA


def sequence_buttons(string):
    buttons_seq = ['1', '11', '111', '1111', '11111', '2', '22', '222', '3', '33', '333', '4', '44', '444', '5', '55', '555', '6', '66', '666', '7', '77', '777', '7777', '8', '88', '888', '9', '99', '999', '9999', '0']
    small_alphabet = ".,?!:abcdefghijklmnopqrstuvwxyz "
    lookup = {}
    for k, v in zip(small_alphabet, buttons_seq):
        lookup[ord(k)] = v
        lookup[ord(k.upper())] = v
    print(lookup)
    return string.translate(lookup)

print(sequence_buttons("Hello, World!") == "4433555555666110966677755531111")