def is_spam_words(text, spam_words, space_around=False):
    if space_around:
        for w in spam_words:
            if " " + w.lower() in text.lower():
                return True
        return False
    else:
        for w in spam_words:
            if w.lower() in text.lower():
                return True
        return False

print(is_spam_words("Молох", ["лох"]))
print(is_spam_words("Молох", ["лох"], True))
print(is_spam_words("Ты лох.", ["лох"]))  # True
print(is_spam_words("Ты лох.", ["лох"], True))  # True