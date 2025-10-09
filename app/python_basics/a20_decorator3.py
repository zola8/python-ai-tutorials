import time
import functools
import logging

from app.python_basics.a20_decorator2 import repeat

logger = logging.getLogger(__name__)

# ------------------------------------- Timing Decorator

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done!"

# ------------------------------------- Logging Decorator

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

# ------------------------------------- Authentication Decorator

def require_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # In real code, you'd check actual authentication
        if not getattr(wrapper, 'is_authenticated', False):
            raise PermissionError("Authentication required")
        return func(*args, **kwargs)
    return wrapper

@require_auth
def sensitive_operation():
    return "Secret data accessed!"

# ------------------------------------- Class-Based Decorators

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello!")

# ------------------------------------- Decorator Chaining

@timer
@log_calls
@repeat(2)
def my_function():
    return "Hello!"

# Equivalent to: my_function = timer(log_calls(repeat(2)(my_function)))


if __name__ == '__main__':
    slow_function()
    print(add(2,3))

    # Usage
    sensitive_operation.is_authenticated = True
    print(sensitive_operation())  # Works

    say_hello()  # say_hello has been called 1 times
    say_hello()  # say_hello has been called 2 times

    my_function()
