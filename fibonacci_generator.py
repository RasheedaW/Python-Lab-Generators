# Generate Fibonacci numbers
def gen_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


# Test the generator
print("Fibonacci Sequence:")
for number in gen_fibonacci(10):
    print("Fibonacci number:", number)
