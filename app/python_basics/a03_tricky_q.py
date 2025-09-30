# ---------------------------
# Exercise 1: Mutable Default Arguments

def add_item(item, target_list=[]):
    target_list.append(item)
    return target_list

list1 = add_item(1)
list2 = add_item(2)
print(list1)
print(list2)

# ---------------------------
# Exercise 2: Integer Caching & Identity

a = 256
b = 256
print(a is b)

c = 257
d = 257
print(c is d)

# ---------------------------
# Exercise 3: List Slicing vs. Assignment

original = [1, 2, 3]
copy = original
copy[:] = [4, 5, 6]
print(original)
print(copy)

# ---------------------------
# Exercise 4: Late Binding Closures

funcs = []
for i in range(3):
    funcs.append(lambda: i)

for f in funcs:
    print(f())

# ---------------------------
# Exercise 5: Tuple Mutability Illusion

t = ([1, 2], [3, 4])
try:
    t[0] += [5]
except TypeError:
    pass

print(t)

# ---------------------------
# Exercise 6: Chained Comparisons

a = 5
b = 3
c = 7
print(a > b == c)

# ---------------------------
# Exercise 7: Exception in Finally

def tricky():
    try:
        return "try"
    finally:
        return "finally"

print(tricky())

# ---------------------------
# Exercise 8: Class vs Instance Attributes

class Counter:
    count = 0
    def __init__(self):
        self.count += 1

c1 = Counter()
c2 = Counter()
print(Counter.count, c1.count, c2.count)

# ---------------------------
# Exercise 9: String Interning Quirk

a = "hello world"
b = "hello world"
print(a is b)

c = "hello"
d = "hello"
print(c is d)

# ---------------------------
# Exercise 10: Generator vs List Comprehension Scope

x = 10
gen = (x for x in range(3))
lst = [x for x in range(3)]
print(x)
print(list(gen))

# ---------------------------
# Exercise 1: The __del__ Trap

class A:
    def __del__(self):
        print("A deleted")

class B:
    def __init__(self):
        self.a = A()
    def __del__(self):
        print("B deleted")

b = B()
del b

def f():
    b = B()
f()

# ---------------------------
# Exercise 2: Metaclass vs Class Decorator Order

def dec(cls):
    print("decorator")
    return cls

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print("metaclass")
        return super().__new__(mcs, name, bases, dct)

@dec
class C(metaclass=Meta):
    pass

# ---------------------------
# Exercise 3: The += on a Key That Doesn’t Exist

d = {}
# d[0] += 1

# ---------------------------
# Exercise 4: Evaluation Order in Chained Assignment

class X:
    def __iadd__(self, other):
        print("iadd called")
        return self

a = [X()]
a[0] += a.append(1)
print(a, "-------\n")

# ---------------------------
# Exercise 5: The sys.modules Hack

import sys
import types

class FakeModule(types.ModuleType):
    def __getattr__(self, name):
        return "surprise!"

sys.modules['secret'] = FakeModule('secret')

# import secret
# print(secret.anything)
# print(secret.foo.bar.baz)

# ---------------------------
# Bonus (Extreme): Bytecode Manipulation

def f():
    return 42

import types
import dis

# Modify f's bytecode to return 100 instead
code = f.__code__

# Create new constants tuple with 100 instead of 42
new_consts = tuple(100 if const == 42 else const for const in code.co_consts)

# Create new code object with modified constants
new_code = types.CodeType(
    code.co_argcount,
    code.co_posonlyargcount,
    code.co_kwonlyargcount,
    code.co_nlocals,
    code.co_stacksize,
    code.co_flags,
    code.co_code,  # same bytecode
    new_consts,    # modified constants
    code.co_names,
    code.co_varnames,
    code.co_filename,
    code.co_name,
    code.co_firstlineno,
    code.co_lnotab,
    code.co_freevars,
    code.co_cellvars
)

# Replace the function's code object
f.__code__ = new_code

# After modification:
print(f())  # Should print 100

# ---------------------------
