# https://docs.python.org/3.15/tutorial/datastructures.html#list-comprehensions
from itertools import chain

# print({x: x ** 2 for x in (2, 4, 6)})

# squares = [x ** 2 for x in range(11)]
# print(squares)


if __name__ == '__main__':
    # 1. Create a list of squares of numbers from 1 to 10.
    print("1", [x ** 2 for x in range(1, 11)])

    # 2. Given the list words = ['apple', 'banana', 'cherry'], create a new list containing the length of each word.
    words = ['apple', 'banana', 'cherry']
    print("2", [len(word) for word in words])

    # 3. Create a list of even numbers from 0 to 20 (inclusive).
    print("3", [num for num in range(21) if num % 2 == 1])

    # 4. Given the list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], create a new list containing only the odd numbers.
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("4", [num for num in numbers if num % 2 == 1])

    # 5. Create a list of tuples (x, x²) for x in the range 1 to 6.
    print("5", [(num, num ** 2) for num in range(7)])

    # 6. Given the string sentence = "The quick brown fox", create a list of the first letter of each word.
    sentence = "The quick brown fox"
    print("6", [word[0] for word in sentence.split()])

    # 7. Flatten the following list of lists into a single list:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("7", list(chain(*matrix)))
    print("7", [num for row in matrix for num in row])
    flattened = []
    for row in matrix:  # First, iterate through each row in the matrix
        for num in row:  # Then, iterate through each number in that row
            flattened.append(num)  # Add each number to our result list
    print("7 loop", flattened)


    # Example 8: Filter and Flatten with Condition
    # Given a list of lists containing integers, create a flattened list that includes only the even numbers greater than 5.
    nested = [[1, 6, 8], [3, 10, 4], [12, 7, 9]]
    # Expected output: [6, 8, 10, 12]
    print("8", [num for row in nested for num in row if num % 2 == 0 and num > 5])


    # Example 9: Cartesian Product with Filtering
    # Create a list of all pairs (x, y) where x is from [1, 2, 3], y is from [4, 5, 6], but only if x + y is odd.
    # ✅ Expected output: [(1, 4), (1, 6), (2, 5), (3, 4), (3, 6)]
    print("9", [(x, y) for x in [1, 2, 3] for y in [4, 5, 6] if (x + y) % 2 == 1])
    print("9", list())


    # Example 3: Extract Unique Vowels from a Sentence
    # Given a sentence, extract all unique vowels (case-insensitive) in the order they first appear.
    sentence = "Hello, how are you today?"
    # ✅ Expected output: ['e', 'o', 'a', 'u']
    # (Note: 'y' is not considered a vowel here; only a, e, i, o, u)
    # 💡 Hint: You’ll need to track seen vowels—but list comprehensions alone can’t maintain state. So this one requires a clever trick or a helper structure!
    vowels = 'aeiou'
    seen = set()
    unique_vowels = [char for char in sentence.lower()
                     if char in vowels and not (char in seen or seen.add(char))]
    print("10", unique_vowels)

    # seen.add(char)
    # → This is the key trick!
    # set.add() returns None (which is falsy).
    # But it mutates the seen set as a side effect.
    # We use or so that if char not in seen, we evaluate seen.add(char) to add it.

    seen = set()
    result = []
    for char in sentence.lower():
        if char in 'aeiou' and char not in seen:
            result.append(char)
            seen.add(char)
    print("10 loop", result)
