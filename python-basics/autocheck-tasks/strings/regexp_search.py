import re


def find_word(text, word):
    match_obj = re.search(word, text)
    return {
         'result': match_obj != None,
    'first_index': None if not match_obj else match_obj.start(),
    'last_index': None if not match_obj else match_obj.end(),
    'search_string': word,
    'string': text,
    }

my_word = 'Python'
my_text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."

print(find_word(my_text, my_word))



def find_all_emails(text):
    result = re.findall("[a-zA-Z]+[a-zA-Z0-9_\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", text) # important dot "." must be escaped otherwise matches any char
    return result

emails_text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'
emails = find_all_emails(emails_text)
expected_result = ['Ima.Fool@iana.org', 'Fool@iana.org', 'first_last@iana.org', 'first.middle.last@iana.or', 'abc111@test.com']
print('\n'.join(emails))

# З метою спрощення приймемо, що:
# використовуємо тільки цифри та символи +, (, ) та -
# телефонний номер починається із символу +
# шаблон телефону символ + потім три цифри 380, символ (, дві цифри, символ ), три цифри, символ -, одна або дві цифри, символ -, дві чи три цифри
# Довжина шаблону телефонного номера завжди 17 символів
def find_all_phones(text):
    # do the matching using the lookahead and limit the count of matched chars by matching anything exactly 17 times
    # seems like is says find whatever matches the non-capturing lookahead and then match 17 chars
    result = re.findall(r"(?=\+380\(\d{2}\)\d{3}-\d{1,2}-\d{2,3}).{17}", text)
    return result

numbers_text = 'Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'
expected_result = ['+380(67)777-7-771', '+380(67)777-77-77', '+380(67)777-77-78']
print(find_all_phones(numbers_text))

# Початок гіперпосилання може бути http:// або https://
# доменне ім'я — це набір латинських букв, цифр, символів підкреслення _ та точок .
# символи точок . не можуть зустрічатися поруч
def find_all_links(text):
    result = []
    prefix = r"(http|https):\/\/"
    body = r"(\w+\.{1})+"
    postfix = r"[a-zA-Z]+"
    regex = re.compile(prefix + body + postfix)
    iterator = re.finditer(regex, text)
    for match in iterator:
        result.append(match.group())
    return result

links_text = 'The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com ' 
links = find_all_links(links_text)
print(links)