#palindrome
#text = "abbca"
#rev = "".join(reversed(text))
#if rev == text:
#    print("palindrome")
#else:
#    print("not palindrome")
from ctypes import pythonapi

text = str(input("Enter a string: "))
rev = ""
for char in text:
   rev = char + rev
print(rev)
if rev == text:
        print("palindrome")
else:
        print("not palindrome")

#text = "python"
#rev = "".join(reversed(text))
#print(rev)

