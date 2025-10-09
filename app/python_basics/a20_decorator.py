def my_decorator(func):
    def wrapper():
        print("Something before the function")
        func()
        print("Something after the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

if __name__ == '__main__':
    # This is equivalent to: say_hello = my_decorator(say_hello)
    say_hello()
