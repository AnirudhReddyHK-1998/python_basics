num = [1, 2, 34, 45, 12]
largest = num[0]
for i in range(len(num)):
    if num[i] > largest:
        largest = num[i]
print(largest)