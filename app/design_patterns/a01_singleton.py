import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # Double-check locking pattern
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialize only once
        if not hasattr(self, 'initialized'):
            self.initialized = True
            # Your initialization code here
            self.value = 0

    def some_method(self):
        return "This is a singleton method"

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


# Usage example
if __name__ == "__main__":
    # Create multiple instances
    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)  # True - same instance

    s1.set_value(42)
    print(s2.get_value())  # 42 - shared state

    print(s1.some_method())  # "This is a singleton method"
