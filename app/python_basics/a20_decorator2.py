def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# ---------------------------------

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

# ---------------------------------

if __name__ == '__main__':
    print(greet("Alice", greeting="Hi"))
    # Before function call
    # After function call
    # Hi, Alice!

    say_hello()
