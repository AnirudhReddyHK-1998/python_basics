
num = [1, 2, 2, 3, 4, 4, 5]
dep = []
for i in range(len(num)):
    if num[i] not in dep:
        dep.append(num[i])
print(dep)


