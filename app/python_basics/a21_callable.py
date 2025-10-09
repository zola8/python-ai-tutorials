class CallableClass:
    def __call__(self, *args, **kwargs):
        print("This method is executed when the instance is called")
        pass


class RegularClass:
    pass


if __name__ == '__main__':
    obj1 = CallableClass()
    obj2 = RegularClass()

    obj1()

    print(callable(obj1))  # True
    print(callable(obj2))  # False
