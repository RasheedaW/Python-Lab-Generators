# Create a multiplier closure
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply


# Test the closure
times3 = make_multiplier(3)
times10 = make_multiplier(10)

print("Multiplier Closure Test")
print("7 times 3:", times3(7))
print("7 times 10:", times10(7))
