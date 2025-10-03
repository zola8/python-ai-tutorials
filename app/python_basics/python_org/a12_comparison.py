a = 1
b = 2
c = 3
d = 4

# Comparisons can be chained
print(c > a == c - b < d * 2)
# c > a - True
# a == c-b - True
# c-b < d*2 - True

# assignment inside expressions must be done explicitly with the walrus operator :=


print((1, 2, 3) < (1, 2, 4))
print([1, 2, 3] < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4) < (1, 2, 4))
print((1, 2) < (1, 2, -1))
print((1, 2, 3) == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))
