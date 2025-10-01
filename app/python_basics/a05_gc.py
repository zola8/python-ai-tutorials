# https://www.geeksforgeeks.org/python/garbage-collection-python/
import gc
import sys


def reference_counting():
    # Reference Counting
    x = [1, 2, 3]
    print(sys.getrefcount(x))

    y = x
    print(sys.getrefcount(x))

    y = None
    print(sys.getrefcount(x))

    print(sys.getrefcount(y))
    print(sys.getrefcount(None))

    # 2
    # 3
    # 2

    # Explanation:
    #
    # x is referenced twice initially (once by x, once by getrefcount()).
    # Assigning y = x increases the count.
    # Setting y = None removes one reference.

    x = [1, 2, 3]
    y = [4, 5, 6]

    x.append(y)
    y.append(x)
    print(sys.getrefcount(x))
    print(sys.getrefcount(y))
    # x contains y and y contains x.
    # Even after deleting x and y, Python won’t be able to free the memory just using reference counting, because each still references the other.



# Create a cycle
def fun(i):
    x = {}
    x[i + 1] = x
    return x


def garbage_collection():
    # Python’s Generational Garbage Collector is designed to deal with cyclic references. It organizes objects into three generations based on their lifespan:
    #
    # Generation 0: Newly created objects.
    # Generation 1: Objects that survived one collection cycle.
    # Generation 2: Long-lived objects.
    # When reference cycles occur, the garbage collector automatically detects and cleans them up, freeing the memory.
    print(gc.get_threshold())
    # (2000, 10, 10)
    # Explanation: It returns the threshold tuple for generations 0, 1 and 2. When allocations exceed the threshold, collection is triggered.
    c = gc.collect()
    print(c)

    for i in range(10):
        fun(i)

    c = gc.collect()
    print(c)



if __name__ == '__main__':
    reference_counting()
    garbage_collection()
