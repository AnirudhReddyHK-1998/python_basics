# def largest_ele(list):
#     largest = list[0]
#     for i in range(len(list)):
#         if list[i] > largest:
#             largest = list[i]
#     return largest
# list = [10, 25, 8, 40, 15]
# print(largest_ele(list))


# def second_largest_ele(numbers):
#     largest = numbers[0]
#     second_largest = float('-inf')
#     for i in range(len(numbers)):
#         if numbers[i] < largest:
#             second_largest = largest
#             largest = numbers[i]
#         elif numbers[i] < second_largest and numbers[i] > largest:
#             second_largest = numbers[i]
#     return second_largest
# numbers = [10, 25, 8, 40, 5, 15]
# print(second_largest_ele(numbers))

# def calculate_price(price, quantity=1):
#     return price * quantity
# print(calculate_price(100))
# print(calculate_price(100, 2))

# def greet_user(name, message= "Welcome"):
#     return f"{message} {name}"
# print(greet_user("anirudh"))
# print(greet_user("anirudh", "Good Morning"))

def calculate_discount(price, discount):
    discount_amount = price * discount / 100
    return price - discount_amount
total = calculate_discount(238, 3)

print(total)






