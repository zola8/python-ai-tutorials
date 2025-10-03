from itertools import combinations, permutations, count, cycle, repeat, accumulate, batched, chain, compress, dropwhile, \
    filterfalse, groupby, islice, pairwise, starmap, takewhile, zip_longest, tee


# https://docs.python.org/3/library/itertools.html#module-itertools

def print_count():
    print("\n--- count ---")
    # count(10) → 10 11 12 13 14 ...
    for c in count(10, 2):
        if c == 20:
            break
        print(c)


def print_cycle():
    print("\n--- cycle ---")
    i = 0
    # cycle('ABCD') → A B C D A B C D A B C D ...
    for c in cycle('ABCD'):
        i += 1
        if i == 12:
            break
        print(c)


def print_repeat():
    print("\n--- repeat ---")
    # repeat(10, 3) → 10 10 10
    for c in repeat('A', 3):
        print(c)


def print_accumulate():
    # The accumulate() function computes accumulated sums (or results of other binary functions) over an iterable.
    # It's useful for running totals, rolling sums, or cumulative products
    print("\n--- accumulate ---")
    num_list = [1, 2, 3, 4, 5]
    #     accumulate([1,2,3,4,5]) → 1 3 6 10 15
    for c in accumulate(num_list):
        print(c)

    print("sum:", sum(num_list))


def print_batched():
    # The batched() function divides an iterable into tuples ("batches") of a certain size. This is useful for chunking data.
    print("\n--- batched ---")
    # batched('ABCDEFG', n=2) → AB CD EF G
    for c in batched('ABCDEFG', 2):
        print(c)


def print_chain():
    # The chain() function combines several iterables into a single iterator
    print("\n--- chain ---")
    # chain('ABC', 'DEF') → A B C D E F
    print(list(chain('AB', ['1', '2'], ['3'])))
    # ['A', 'B', '1', '2', '3']

    nested = [[1, 2], [3, 4], [5]]
    print(list(chain.from_iterable(nested)))
    # Output: [1, 2, 3, 4, 5]


def print_compress():
    # This is useful when you need to mask/filter data based on some criteria or flags
    print("\n--- compress ---")
    data = ['a', 'b', 'c', 'd']
    selectors = [1, 0, 1, 0]
    print(list(compress(data, selectors)))
    # Output: ['a', 'c']


def print_dropwhile():
    # The dropwhile() function drops elements from the start of an iterable as long as a specified condition is true;
    # once the condition becomes false, it returns the rest of the iterable without further checks.
    print("\n--- dropwhile ---")
    data = [1, 2, 3, 5, 6, 7]
    result = dropwhile(lambda x: x < 5, data)
    print(list(result))
    # Output: [5, 6, 7]
    words = ["apple", "banana", "Cherry", "Date", "Elderberry"]
    filtered = dropwhile(lambda s: s[0].islower(), words)
    print(list(filtered))
    # Output: ['Cherry', 'Date', 'Elderberry']
    # Data Cleaning: In log file processing, dropwhile can skip initial rows
    # Parsing Files: Used to discard file headers


def print_takewhile():
    print("\n--- takewhile ---")
    print(list(takewhile(lambda x: x < 5, [1, 4, 6, 3, 8])))  # [1, 4]


def print_filterfalse():
    # The filterfalse() function filters elements by returning only those for which the predicate function returns False.
    # Example filtering out even numbers (keeping odd numbers).
    print("\n--- filterfalse ---")
    numbers = [1, 2, 3, 4, 5, 6]
    odds = filterfalse(lambda x: x % 2 == 0, numbers)
    print(list(odds))
    # Output: [1, 3, 5]
    # Filtering Invalid Data: When screening datasets, filterfalse easily removes unwanted elements such as non-matching records
    # Data Analysis: Used in inverse filtering, such as finding all non-prime numbers from a sequence


def print_groupby():
    print("\n--- groupby ---")
    # Note: Elements must be sorted by the key function for meaningful groups.
    # Reporting and Summarization: Frequently used for grouping database query results or CSV data by a certain key
    # Log Analysis: Grouping log entries by error type, date, or user for easier error tracking
    data = [('A', 1), ('A', 2), ('B', 3), ('B', 4), ('C', 5)]
    for key, group in groupby(data, key=lambda x: x[0]):
        print(key, list(group))
    # Output:
    # A [('A', 1), ('A', 2)]
    # B [('B', 3), ('B', 4)]
    # C [('C', 5)]

    # Example grouping words by their first letter:
    words = ['apple', 'apricot', 'banana', 'berry', 'cherry']
    groups = groupby(sorted(words), key=lambda x: x[0])
    for letter, group in groups:
        print(letter, list(group))
    # Output:
    # a ['apple', 'apricot']
    # b ['banana', 'berry']
    # c ['cherry']


def print_islice():
    #     The islice() function slices an iterable like a list slice but returns an iterator rather than a list.
    # Processing Large Files: Efficiently extracting a subset of rows from large files or streams (e.g., previewing first 100 records) without loading everything into memory.
    # Data Sampling: Used for pulling out every nth item, creating quick training/testing datasets
    # Pagination: Splitting long lists for paginated results in applications or APIs
    print("\n--- islice ---")
    data = range(10)
    first_three = islice(data, 3)
    print(list(first_three))
    # Output: [0, 1, 2]
    sliced = islice(data, 2, 7)
    print(list(sliced))
    # Output: [2, 3, 4, 5, 6]


def print_pairwise():
    print("\n--- pairwise ---")
    # pairwise('ABCDEFG') → AB BC CD DE EF FG
    print(list(pairwise('ABCDEFG')))
    data = [1, 2, 3, 4]
    print(list(pairwise(data)))  # [(1, 2), (2, 3), (3, 4)]
    # This function is useful in scenarios like processing consecutive elements for comparison, finding differences


def print_starmap():
    print("\n--- starmap ---")
    # Use starmap to apply a function to unpacked arguments from tuples in an iterable, especially when functions take multiple parameters.
    # It is like map, but the function is called with multiple arguments unpacked from each tuple.
    pairs = [(2, 3), (4, 2)]
    print(list(starmap(pow, pairs)))  # [8, 16]
    #   geometric points where each tuple represents coordinates
    # This saves you from manually unpacking tuples for each call and works well in functional programming and multiprocessing contexts


def print_zip_longest():
    print("\n--- zip_longest ---")
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b', 'c']
    print(list(zip_longest(list1, list2, fillvalue='-')))
    # Result: [(1, 'a'), (2, 'b'), (3, 'c'), (4, '-'), (5, '-')]
    #     This is useful when combining sequences of different lengths, ensuring no data from the longest iterable is lost and providing a fill for missing elements.


def print_tee():
    # The function itertools.tee splits one iterator into multiple independent iterators (defaults to 2).
    # This allows you to iterate over the original iterator multiple times independently without consuming it.
    # This is helpful when you need to reuse the data from a single iterable multiple times in different contexts without recreating the iterable.
    print("\n--- tee ---")
    original = iter([1, 2, 3, 4])
    iter1, iter2 = tee(original)
    print(list(iter1))  # Output: [1, 2, 3, 4]
    print(list(iter2))  # Output: [1, 2, 3, 4]


def print_zip():
    # zip(iterable1, iterable2, ...)
    # Combine two lists into pairs:
    names = ['Alice', 'Bob', 'Charlie']
    scores = [85, 90, 88]
    zipped = list(zip(names, scores))
    print(zipped)

    # Iterate over multiple lists simultaneously:
    for name, score in zip(names, scores):
        print(f"{name} scored {score}")

    # Create a dictionary from two lists (one for keys, one for values):
    keys = ['id', 'name', 'age']
    values = [101, 'Alice', 25]
    dictionary = dict(zip(keys, values))
    print(dictionary)
    # Output: {'id': 101, 'name': 'Alice', 'age': 25}

    # Unzip a zipped object using the unpacking operator *:
    zipped = [('a', 1), ('b', 2), ('c', 3)]
    letters, numbers = zip(*zipped)
    print(letters)  # ('a', 'b', 'c')
    print(numbers)  # (1, 2, 3)


if __name__ == '__main__':
    # print_count()
    # print_cycle()
    # print_repeat()
    # print_accumulate()
    # print_batched()
    # print_chain()
    # print_compress()
    # print_dropwhile()
    # print_takewhile()
    # print_filterfalse()
    # print_groupby()
    # print_islice()
    # print_pairwise()
    # print_starmap()
    # print_zip_longest()
    # print_tee()
    print_zip()
