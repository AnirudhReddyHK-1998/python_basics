num = {1:2, 2:2, 3:2, 4:3, 5:1, 6:2, 7:4}
nums = int(input("Enter a number: "))

count = 0
for i in num.values():
    if i == nums:
        count = count + 1

print(count)

