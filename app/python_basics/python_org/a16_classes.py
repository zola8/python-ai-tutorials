from dataclasses import dataclass


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


@dataclass
class Employee:
    name: str
    dept: str
    salary: int


if __name__ == '__main__':
    mapping = Mapping(range(10))
    mapping.update(range(3))
    print(mapping.items_list)

    mapping = MappingSubclass(range(10))
    mapping.update([1,2,3], ['a','b','c'])
    print(mapping.items_list)

    john = Employee('john', 'computer lab', 1000)
    print(john)
