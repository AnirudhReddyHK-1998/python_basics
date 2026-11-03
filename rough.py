#frequency count of single value
# num = {1:2, 2:2, 3:2, 4:3, 5:1, 6:2, 7:4}
# nums = int(input("Enter a number: "))
#
# count = 0
# for i in num.values():
#     if i == nums:
#         count = count + 1
#
# print(count)
# # #
#
#palindrome using ::-1
# text = "madam"
# palin = text[::-1]
# if palin == text:
#     print("palindrome")
# else:
#     print("not palindrome")
#

#frequency count of letters
# text = "bananna"
# dic = {}
# for i in range(len(text)):
#     if text[i] in dic:
#         dic[text[i]] += 1
#     else:
#         dic[text[i]] = 1
# print(dic)

#second largest in the list
# num = [30, 10, 20, 5, 4]
#
# largest = num[0]
# second_largest = float('-inf')
#
# for i in range(len(num)):
#     if num[i] > largest:
#         second_largest = largest
#         largest = num[i]
#
#     elif num[i] > second_largest and num[i] < largest:
#         second_largest = num[i]
#
# print("Second largest:", second_largest)

#finding largest and smallest
num = [15, -5, 30, 2, 100, -20]
largest = num[0]
smallest = num[0]
for i in range(len(num)):
    if num[i] > largest:
        largest = num[i]
    elif num[i] < smallest:
        smallest = num[i]
print("largest", largest)
print("smallest", smallest)