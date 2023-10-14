fruits = ["mango", "kiwi", "strawberry", "guava", "pinapple", "mandarin", "orange"]
# dict word to its lenth

# loop solution 
res_dict = dict()
for fruit in fruits:
    res_dict[fruit] = len(fruit)
print(res_dict)

# dict comprehension solution
result = { fruit : len(fruit) for fruit in fruits }

# dict word by index
word_by_index = { index : word for index, word in enumerate(fruits)}
index_by_word = { word : index for index, word in enumerate(fruit)}

# repacking the dictionary into another dictionary with comprehension
# TODO: check how to repackage dict with list comprehension
# ever_or_odd_index_by_word = { (word : "even" if index % 2 == 0 else word : "odd") for word, index in word_by_index}