fib_count = int(input("Fibonacci from: "))

a = 0
b = 1

for i in range(fib_count):
    print(a)
    a, b = b, a + b
    # Update a and b here