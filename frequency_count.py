num = [1, 2, 2, 3, 1, 2, 4]
dep = {}

for i in range(len(num)):
    if num[i] in dep:
        dep[num[i]] = dep[num[i]] + 1
    else:
        dep[num[i]] = 1

print(dep)