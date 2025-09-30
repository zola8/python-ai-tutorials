# https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/in-class-questions-and-video-solutions/lecture-5/

def always_sunny(t1, t2):
    """ t1, t2 are non empty """
    sun = ("sunny", "sun")
    first = t1[0] + t2[0]
    return (sun[0], first)


print(always_sunny(('cloudy'), ('cold',)))
# ('sunny', 'ccold')

# --------------------------

L = ["life", "answer", 42, 0]
for thing in L:
    if thing == 0:
        L[thing] = "universe"
    elif thing == 42:
        L[1] = "everything"


print(L)
# ['universe', 'everything', 42, 0]

# --------------------------

class Animal:
    pass

class Dog(Animal):
    def speak(self):
        print("ruff ruff")

d = Dog(7)
d.set_name("Ruffles")
d.speak()
