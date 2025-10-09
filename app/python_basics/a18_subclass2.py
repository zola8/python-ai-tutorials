def final(cls):
    """Decorator to make a class final (cannot be subclassed)"""

    def __init_subclass__(cls, **kwargs):
        raise TypeError(f"Cannot subclass final class {cls.__name__}")

    cls.__init_subclass__ = classmethod(__init_subclass__)
    return cls


@final
class FinalClass:
    pass


# This works fine
obj = FinalClass()


# This raises TypeError: Cannot subclass final class DerivedClass
class DerivedClass(FinalClass):
    pass

# Using __init_subclass__ with a decorator pattern
