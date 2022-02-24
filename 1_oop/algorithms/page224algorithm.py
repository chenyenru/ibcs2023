# max = 10
# sum = 0
# count = 0

# for count in range(max-4+1):
#     sum = max-4
#     count = max-3
#     for sum in range(3,5):
#         if count == 0 and max > 0:
#             print("hello")
#         elif count<4:
#             print("go for it")
#         else:
#             print("OK")
# sum += count
# print("total = ", sum)
# print("max = ", count)


max = 10
sum = 0
count = 0

while count < (max - 4 + 1):
    sum = max - 4
    count = max - 3

    sum = 3
    while sum < (4 + 1):
        if count == 0 and max > 0:
            print("Hello")
        elif count < 4:
            print("Go for it")
        else:
            print("OK")
        sum += 1
    count += 1

sum = sum + count
print(f"Total = {sum}")
print(f"Max = {count}")
