from time import time, sleep


def extend_print(func):
    print(func.__name__)

    def wrapper(a, b):
        print("Before execution")  # decoration
        result = func(a, b)  # execution of the function
        print("Before execution")  # decoration
        return result
    return wrapper


@extend_print
def print_full_name(name, surname):
    print(f"{name}{surname}")


print_full_name("Lada", "Murchych")


def measure_exec_time(func):
    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__, "executed in ", time() - t)
        return result
    return wrapper


@measure_exec_time
def sleep_function(sleep_time):
    print("Before sleep...")
    sleep(sleep_time)
    print("Finally awake!")


sleep_function(1)


@measure_exec_time
def fibonacci(n):
    def _fibonacci(n): # have to wrap the recursive call into the outer function
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return _fibonacci(n - 1) + _fibonacci(n - 2)

    return _fibonacci(n)


res = fibonacci(40) # takes 21 seconds!!!
print(res)


def percent(func):
    def inner(*args, **kwargs):
        print('%'*15)
        func(*args, **kwargs)
        print('%'*15)
    return inner


def star(func):
    def inner(*args, **kwargs):
        print('*'*15)
        func(*args, **kwargs)
        print('*'*15)
    return inner


@percent
@star
def table_header(title):
    print(title)


table_header(f"{'My New Table':^15}")
