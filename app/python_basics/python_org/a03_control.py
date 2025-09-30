words = ['cat', 'window', 'zürichstrasse']
for w in words:
    print(w, len(w))

print("------")

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user, status in users.items():
    print(user, status)

print("------")

for i in range(3):
    print(i)

print(range(5))
print(list(range(5)))

print("sum:", sum(range(5)))

print("------")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

print("------")

for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

print("------")

# for-break-else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

print("------")

# https://docs.python.org/3.15/tutorial/controlflow.html#pass-statements
def initlog():
    print("Initializing log 1")
    pass   # Remember to implement this!

# https://docs.python.org/3.15/library/stdtypes.html#the-ellipsis-object
def initlog2():
    print("Initializing log 2")
    ...

def initlog3():
    print("Initializing log 3")
    return NotImplemented

def initlog4():
    print("Initializing log 4")
    raise NotImplementedError

initlog()
initlog2()
initlog3()
initlog4()
