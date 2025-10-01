from itertools import combinations, permutations, product


# https://docs.python.org/3/library/itertools.html#module-itertools


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


def print_variation():
    # product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) → 000 001 010 011 100 101 110 111
    print("\n--- product (variation) ---")
    print(list(product('ABCD', repeat=2)))
    # AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
    #     Öt betűből alkotható hárombetűs "szavak" egy-egy (ismétléses) variációt alkotnak.
    # A halmaz elemiből k darabot sorban egymás után felírunk, akkor variációnak nevezzük az így kapott sorozatot.
    # Ha az elemeket ki is emeljük a halmazból, akkor lesz a variáció ismétlés nélküli.


if __name__ == '__main__':
    # print_combinations()
    # print_permutations()
    print_variation()

    print()
