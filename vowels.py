text = str(input("Enter a text: ")).lower()
count = 0
for char in text:
    if char in "aeiou":
        count = count + 1
print(count)


