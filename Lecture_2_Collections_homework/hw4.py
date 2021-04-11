"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from inspect import getfullargspec
from collections.abc import Callable

c = {}

def cache(func: Callable) -> Callable:
    if callable(func):
        c[func.__name__] = func, {}
        arguments = getfullargspec(func)[0];
        def bar(*arguments):
            global c
            if arguments not in c[func.__name__][1]:
                c[func.__name__][1][arguments] = func(*arguments)
            return c[func.__name__][1][arguments];
        return bar
    else:
        raise ValueError("func must be Callable")
    
