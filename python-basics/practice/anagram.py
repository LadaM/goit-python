from collections import Counter
# abc and bca are anagram

def is_anagram(w1, w2):
    return Counter(w1) == Counter(w2)

# print(is_anagram("abc", "bca"))

def is_anagram_with_set(w1, w2):
    return len(w1) == len (w2) and set(w1) == set(w2)

# print(is_anagram_with_set("aad", "add")) # --> will give wrong result

def is_anagram_ord(w1, w2):
    return len(w1) == len(w2) and sum([ord(char) for char in w1]) == sum([ord(char) for char in w2])
print(is_anagram_ord("sass", "ssss"))