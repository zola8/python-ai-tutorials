import threading


def hello_world():
    print("Hello, world!")


if __name__ == '__main__':
    t = threading.Thread(target=hello_world)
    t.start()

# To run a function in a thread:
# Import the threading module.
# Define the function for the thread to execute.
# Create a Thread object, passing the function as its target.
# Start the thread using the start() method.

# Threading Limitations:
# In CPython (the standard Python implementation), a Global Interpreter Lock (GIL) exists, meaning only one thread can execute Python bytecode at a time, which limits true parallelism for CPU-bound work.
# Threading is best suited for I/O-bound programs—tasks that spend time waiting for input/output operations, rather than heavy computation.
# For CPU-bound tasks, multiprocessing or concurrent futures is recommended.
