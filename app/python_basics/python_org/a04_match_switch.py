# https://docs.python.org/3.15/tutorial/controlflow.html#match-statements
# Only the first pattern that matches gets executed

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"


print(http_error(400))
print(http_error(401))
print(http_error(418))

print("------")


def check_point(point: (int, int)):
    # point is an (x, y) tuple
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")


check_point((0, 0))
check_point((0, 10))
check_point((10, 0))
check_point((20, 30))

print("------")

month = 5
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")

print("------")

# * may also be _ matches a sequence of at least two items without binding the remaining items

def alma(a, b, *rest):
    print(a, b, *rest)

alma(1, 2, 3, 4, 5)

