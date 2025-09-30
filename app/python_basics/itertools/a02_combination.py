from itertools import combinations, permutations, count, cycle, repeat, accumulate, batched


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


def print_combinations():
    # a kombinációnál a sorrend nem számít
    # egy halmazból adott számú elemet választunk ki úgy, hogy a sorrend nem számít.
    # Például egy lottószelvényen a kihúzott számok sorrendje nem számít, csak az, hogy mely számokat húzták ki.

    print("\n--- combinations ---")
    for c in combinations('ABCD', 2):
        print(c)

    # ('A', 'B')
    # ('A', 'C')
    # ('A', 'D')
    # ('B', 'C')
    # ('B', 'D')
    # ('C', 'D')


def print_permutations():
    # a permutáció esetén a sorrend számít
    # Például, ha három ember (András, Béla, Cecília) sorrendjét nézzük egy versenyben, akkor a sorrendben bekövetkező változások külön permutációnak számítanak.

    print("\n--- permutations ---")
    for c in permutations('ABCD', 2):
        print(c)

    # ('A', 'B')
    # ('A', 'C')
    # ('A', 'D')
    # ('B', 'A')
    # ('B', 'C')
    # ('B', 'D')
    # ('C', 'A')
    # ('C', 'B')
    # ('C', 'D')
    # ('D', 'A')
    # ('D', 'B')
    # ('D', 'C')

def print_accumulate():
    print("\n--- accumulate ---")
    num_list = [1,2,3,4,5]
    #     accumulate([1,2,3,4,5]) → 1 3 6 10 15
    for c in accumulate(num_list):
        print(c)

    print("sum:", sum(num_list))



def print_batched():
    print("\n--- batched ---")
    # batched('ABCDEFG', n=2) → AB CD EF G
    for c in batched('ABCDEFG', 2):
        print(c)



if __name__ == '__main__':
    # print_combinations()
    # print_permutations()
    # print_count()
    # print_cycle()
    # print_repeat()
    # print_accumulate()
    print_batched()

    print()