class Valami():

    @classmethod
    def print_hello(cls):
        print("hello")


if __name__ == '__main__':
    Valami.print_hello()
    Valami().print_hello()

# The @classmethod form is a function decorator
