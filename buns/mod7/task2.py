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


@memoize
def fibonacci(n):
    """Вычислите n-е число Фибоначчи"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)