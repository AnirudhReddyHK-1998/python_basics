
#number = float(input("Enter a number: "))
#if number % 2 == 0:
 #   print("Even")
#else:
 #   print("Odd")


value = list(map(int, input("Enter Numbers: ").split()))
largest = value[0]
for num in value:
    if num > largest:
        largest = num
print("The largest number is ", largest)

#palindrome
text = "abba"
rev = reversed(text)
print(rev)
