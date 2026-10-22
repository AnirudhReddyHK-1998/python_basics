
#num = [1, 2, 2, 3, 4, 4, 5]
#dep = []
#for i in range(len(num)):
 #   if num[i] not in dep:
 #       dep.append(num[i])
#print(dep)

num = [1, 2, 2, 3, 1, 2, 4]
dep = {}

for i in range(len(num)):
    if num[i] in dep:
        dep[num[i]] = dep[num[i]] + 1
    else:
        dep[num[i]] = 1

print(dep)