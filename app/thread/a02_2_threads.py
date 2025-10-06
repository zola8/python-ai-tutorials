import threading
import time


def print_even():
    for i in range(0, 10, 2):
        print(f"Even: {i}")
        time.sleep(1)


def print_odd():
    for i in range(1, 10, 2):
        print(f"Odd: {i}")
        time.sleep(1)


if __name__ == '__main__':
    # Create two threads
    thread1 = threading.Thread(target=print_even)
    thread2 = threading.Thread(target=print_odd)

    # Start both threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    print("Both threads are done!")
