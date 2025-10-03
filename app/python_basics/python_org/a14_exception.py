# https://docs.python.org/3.15/tutorial/errors.html

def this_fails():
    try:
        x = 1/0
    except ZeroDivisionError as err:
        print('Handling run-time exception:', err)


class MyException(Exception):
    pass


def my_raising_exception():
    raise MyException('my z exception')



def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


if __name__ == '__main__':
    # while True:
    #     try:
    #         x = int(input("Please enter a number: "))
    #         break
    #     except (RuntimeError, TypeError, NameError):
    #         print("???")
    #     except ValueError:
    #         print("Oops!  That was no valid number.  Try again...")

    this_fails()

    try:
        my_raising_exception()
    except MyException as err:
        print('Handling exception:', err)

    divide(5, 10)
    divide(5, 0)
