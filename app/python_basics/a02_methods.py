from datetime import date

# https://stackoverflow.com/questions/54264073/what-is-the-use-and-when-to-use-classmethod-in-python

class Person():
    species='homo_sapiens' # This is class variable
    def __init__(self, name, age):
        self.name = name # This is instance variable
        self.age = age

    def show(self):
        print('Name: {}, age: {}.'.format(self.name, date.today().year - self.age))

    @classmethod
    def create_with_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    @classmethod
    def print_species(cls):
        print('species: {}'.format(cls.species))

    @staticmethod
    def get_birth_year(age):
        return date.today().year - age


if __name__ == '__main__':
    navy = Person.create_with_birth_year('Navy Cheng', 1989)
    navy.show()

    Person.print_species()

    print(Person.get_birth_year(100))

# Instance method
# Class method
# Static Method
