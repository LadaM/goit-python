import re


def replace_spam_words(text, spam_words):
    regexp = rf"{'|'.join(spam_words)}"
    print(re.findall(regexp, text))
    print(regexp)
    return re.sub(regexp, lambda m: "*" * len(m.group()), text, count = 0, flags=re.IGNORECASE)

colors = ['blue', 'red', 'white']
sentence = 'blue socks and RED shoes, white T-shirt and blue jeans, red cap'

print(replace_spam_words(sentence, colors))
