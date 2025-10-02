from math import copysign

print(round(1.4), round(1.6))
# 1 2

print(round(0.5), round(1.5), round(2.5))


# 0 2 2

# rounding to closest, ties away from zero -- other algorithms
# Banker’s Rounding -- python
# https://medium.com/@akhilnathe/understanding-pythons-round-function-from-basics-to-bankers-b64e7dd73477


def _round(number):
    return int(number + 0.5 * copysign(1, number))


print("--- conventional_round")
print(round(1.5), _round(1.5))
print(round(2.5), _round(2.5))

f: float = 2.5
print(f == 2.50)
