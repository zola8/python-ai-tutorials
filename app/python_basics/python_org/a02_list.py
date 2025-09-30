# https://docs.python.org/3.15/tutorial/introduction.html#lists

squares = [1, 4, 9, 16, 25]
print(squares[-3:])

rgb = ["Red", "Green", "Blue"]
rgba = rgb
rgba.append("Alph")

# All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list:
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(rgba)
print(correct_rgba)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
# clear the list by replacing all the elements with an empty list
letters[:] = []
print("letters:", letters)


a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(len(x))
print(x[0][1]) # b


# Fibonacci series:
# the sum of two elements defines the next
print("Fibonacci series")
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
# multiple assignment, the right side evaluated first!
