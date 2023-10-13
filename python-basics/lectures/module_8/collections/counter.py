import collections

marks = [1, 2, 3, 4, 4, 4, 5, 3, 5, 3, 6, 2, 3, 5, 5, 3, 4, 3, 3, 3, 1]
# to aggregate the marks into count by mark before we needed to make a following cycle
mark_counts = {}
for m in marks:
    if m in mark_counts:
        mark_counts[m] += 1
    else:
        mark_counts[m] = 1
print(mark_counts)

# simpler solution would be to use the Counter from collections
# just create a new Counter from anything that can be iterated over
counts = collections.Counter(marks)
print(counts)
print(f"most common mark is {counts.most_common()}")


# having a word we can count the number of letters in the text
letters = collections.Counter("Mississippi")
print(letters)