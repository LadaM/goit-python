import re

def sanitize_phone_number(phone):
    return re.sub("[+\-()\" ]", "", phone)

print(sanitize_phone_number('      +38(050)123    -32-34"   '))


def sanitize_phone_number(phone):
    # using the built-in string methods the implementation is a bit more verbose
    return phone.strip(' ,+"()-').replace('-','').replace('(', '').replace(')', '').replace(' ', '')

print(sanitize_phone_number('      +38(050)123    -32-34"   '))


