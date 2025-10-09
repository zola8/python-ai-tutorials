class FinalClass:
    def __init_subclass__(cls, **kwargs):
        raise TypeError(f"Cannot subclass {cls.__name__}")

# This works fine
obj = FinalClass()

# This raises TypeError: Cannot subclass DerivedClass
class DerivedClass(FinalClass):
    pass

