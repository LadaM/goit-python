# num = int(input("Enter integer (0 for output): "))
# sum = 0
# while num != 0: 
#     for n in range(1, num):
#         sum = sum + n
#     print(sum)    
#     num = int(input("Enter integer (0 for output): "))

num = int(input("Enter integer (0 for output): "))
sum = 0
while num > 0:
    for i in range(num + 1):
        sum += i
    # validation not necessery since the task is to accumulate all sums of 0..N
    # if sum != int((num * (num +1)) / 2):
        # print("Wrong sum!")
    num = int(input("Enter integer (0 for output): "))

# alternative solution using break
sum = 0
while True:
    # we will execute this loop at least once
    num = int(input("Enter integer (0 for output): "))
    if num is 0:
        break
    for i in range(num + 1):
        sum = sum + i
