# https://docs.python.org/3.15/tutorial/datastructures.html

list1 = [10, None, "alma", 5, "poker"]
# list.sort()
# TypeError: '<' not supported between instances of 'NoneType' and 'int'

print(list1)



squares = []
for x in range(10):
    squares.append(x**2)

print(x)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)



# https://docs.python.org/3.15/tutorial/datastructures.html#tuples-and-sequences
# tuple:
t = 12345, 54321, 'hello!'
print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# The expression (()) is not a nested tuple, it is a single tuple surrounded by parentheses
# A single item tuple must have a trailing comma, such as (d,)
print(((())) == ())

# () == tuple()
# (()) == (tuple()) == tuple()  # outer parens unnecessarily groups the empty tuple
# ((),) == (), == tuple(tuple()) # the comma creates a single element tuple containing the empty tuple
# [] == list()
# [[]] == [[],] == list(list) # the comma here is optional since the constructor is the square brackets
