# https://stackoverflow.com/questions/27536852/pycharm-and-debugging-private-attributes
# https://en.wikipedia.org/wiki/Name_mangling#Real-world_effects_of_C++_name_mangling

class Box:
    def __init__(self, a, b, c):
        self.__a = a
        self._b  = b
        self.c   = c
        d = 0 #Breakpoint.



if __name__ == '__main__':
    a = Box(1, 2, 3)
