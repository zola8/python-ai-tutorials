# Membership test operations
# https://docs.python.org/3.15/reference/expressions.html#membership-test-operations

print(3 not in [2, 3, 4])

print(3 not in [4, 5, 6])

print((2, 3) not in [(2, 3), (5, 6), (9, 1)])

print((2, 3) not in [(2, 7), (7, 3), "hi"])


# https://docs.python.org/3.15/tutorial/controlflow.html#positional-or-keyword-arguments
# Positional-or-Keyword Arguments
def alma(name, color):
    print(name, color)


alma("pink lady", "red")
alma(name="pink lady", color="red")


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)


# combined_example(pos_only=1, standard=2, kwd_only=3)


# TypeError: foo() got multiple values for argument 'name'
# def foo(name, **kwds):

def foo(name, /, **kwds):
    print('name' in kwds)
    return 'name' in kwds


foo(1, **{'name': 2})


# a function can be called with an arbitrary number of arguments. These arguments will be wrapped up in a tuple.
# Before the variable number of arguments, zero or more normal arguments may occur.
# tuple = all remaining input arguments that are passed to the function

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus", sep="."))


# https://docs.python.org/3.15/tutorial/controlflow.html#unpacking-argument-lists
# Unpacking Argument Lists -  the arguments are already in a list or tuple but need to be unpacked for a function call
# dictionaries can deliver keyword arguments with the **-operator

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
