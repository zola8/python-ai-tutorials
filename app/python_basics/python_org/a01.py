# https://docs.python.org/3.15/tutorial/introduction.html

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

s = 3 * 'un' + 'ium'
print(s)

s = 'un' * 2 + 'ium'
print(s)

print(type(5))
print(type(s))

print(3.0-1)

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
ss = 'Py'   'thon'
print(ss)

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

word = 'Python'
print(word[0])  # character in position 0
print(word[-2])  # second-last character
print(word[0:2])  # slicing, characters from position 0 (included) to 2 (excluded)

# s[:i] + s[i:] is always equal to s:
print(word[:2] + word[2:])

#       +---+---+---+---+---+---+
#       | P | y | t | h | o | n |
#       +---+---+---+---+---+---+
#         0   1   2   3   4   5
#        -6  -5  -4  -3  -2  -1

number = 1_000_000
number += 2
print(number)

# https://docs.python.org/3.15/reference/lexical_analysis.html#named-unicode-character
print('\N{SNAKE}')
print('\U0001f40d')
print('\u1234')

# all unrecognized escape sequences are left in the string unchanged
print('\q')

print(list(b'\x89PNG\r\n\x1a\n'))
# [137, 80, 78, 71, 13, 10, 26, 10]

# Raw string literals
print(r'\d{4}-\d{2}-\d{2}')

print(f"formatting: {65:#0x}")
# 0x41

print(7922816251426433759354395033679228162514264337593543950336 * 3445756)
print(3.14_15_92_63)

print(1.0e3)  # (represents 1.0×10³, or 1000.0)
print(1.166e-5)  # (represents 1.166×10⁻⁵, or 0.00001166)
