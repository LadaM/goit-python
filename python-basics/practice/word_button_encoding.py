btns_symbols = {
    1:	".,?!:",
2	:'ABC',
3	:'DEF',
4	:'GHI',
5	:'JKL',
6	:'MNO',
7	:'PQRS',

8	:'TUV',
9	:'WXYZ',
0	:' ',
}

def encode_message_with_btns(message):
    for char in message:
        for k, v in btns_symbols:
            if char in v:
                pass # have to "press" the button number of times