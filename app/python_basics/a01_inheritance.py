class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")

class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("second")

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
        print("third")


if __name__ == '__main__':
    Third()

# second
# first
# third

# https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance
