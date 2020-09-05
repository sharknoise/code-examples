from functools import wraps


def suppress(exception, *, or_return=None):
    """Suppress exceptions of provided class(es) and return a value instead."""
    def wrapper(function):
        @wraps(function)
        def inner(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except exception:
                return or_return
        return inner
    return wrapper


@suppress(ZeroDivisionError, or_return=42)
def foo():
     return 1 // 0

print(foo())  # 42