import time


def validate_args(func):
    def wrapper(*args, **kwargs):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"

        if not isinstance(args[0], int):
            return "Wrong types"

        if args[0] < 0:
            return "Negative argument"

        return func(*args, **kwargs)

    return wrapper

class Timer:
    def __init__(self, func):
        self.func = func
        self.start = None
        self.end = None

    def __call__(self, *args, **kwargs):
        if self.start is None:
            self.start = time.time()
            result = self.func(*args, **kwargs)
            self.end = time.time()
            print(f"Функция {self.func.__name__!r} выполнялась {(self.end - self.start):.4f} секунд")
            self.start = None
            self.end = None
        else:
            result = self.func(*args, **kwargs)
        return result


def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    memoized_func.__name__ = func.__name__
    memoized_func.__doc__ = func.__doc__
    return memoized_func


@validate_args
@Timer
@memoize
def fibonacci(n):
    """Calculate the nth Fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(30)) # с декоратором memoize


@Timer
def fibonacci_no_memoize(n):
    if n < 2:
        return n
    return fibonacci_no_memoize(n - 1) + fibonacci_no_memoize(n - 2)

print(fibonacci_no_memoize(30)) # без декоратора memoize