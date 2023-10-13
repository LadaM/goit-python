import random

count_heads = 0
count_tails = 0

coin_tosses = {
    1: "Heads", 
    2: "Tails"
}
# to keep track of the results
sequence = list()

streak = 3
while count_heads < streak and count_tails < streak:
    choice = random.randint(1, 2)
    if choice == 1:
        count_heads += 1
        count_tails = 0
    else:
        count_tails += 1
        count_heads = 0
    sequence.append(coin_tosses[choice])
print(f"Made {len(sequence)} attempts to get streak of {stre}")
