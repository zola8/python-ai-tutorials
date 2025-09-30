# https://docs.python.org/3.15/tutorial/controlflow.html#lambda-expressions
# Small anonymous functions can be created with the lambda keyword

# lambda arguments: expression
# arguments: comma-separated parameters (like regular functions)

# Regular function
def add(x, y):
    return x + y

# Equivalent lambda
add_lambda = lambda x, y: x + y

print(add(3, 5))        # Output: 8
print(add_lambda(3, 5)) # Output: 8

# -----------------------------

# No Parameters
get_pi = lambda: 3.14159
print(get_pi())  # Output: 3.14159

# -----------------------------

# With map() - Transform Lists
# Apply function to every item of iterable and return a list of the results.
# map(function, iterable, ...)

numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Convert to strings
strings = list(map(lambda x: str(x), numbers))
print(strings)  # Output: ['1', '2', '3', '4', '5']

# -----------------------------

# map = is basically equivalent to:
# [f(x) for x in iterable]
# [(a, b) for a in iterable_a for b in iterable_b]

# result = []
# for a in iterable_a:
#     for b in iterable_b:
#         result.append((a, b))

# -----------------------------

