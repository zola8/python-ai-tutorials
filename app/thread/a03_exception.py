import threading

# Store any exceptions here
thread_exceptions = []


def safe_run(target, *args):
    try:
        target(*args)
    except Exception as e:
        thread_exceptions.append((threading.current_thread().name, str(e)))


def raises_error():
    raise ValueError("Something went wrong in raises_error!")


def runs_fine():
    print("runs_fine completed successfully")


if __name__ == '__main__':
    # Create and start threads, each wrapped in safe_run for exception capture
    t1 = threading.Thread(target=safe_run, args=(raises_error,), name='Thread-1')
    t2 = threading.Thread(target=safe_run, args=(runs_fine,), name='Thread-2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # Handle all thread exceptions in the main thread
    if thread_exceptions:
        for thread_name, err in thread_exceptions:
            print(f"Exception in {thread_name}: {err}")
    else:
        print("No exceptions occurred.")


# Each thread is started with a safe_run wrapper, which catches any exceptions and stores them in a shared list.
# After both threads finish, the main thread checks thread_exceptions to report or process any errors that occurred in either thread.
