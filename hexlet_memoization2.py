"""
В этот раз вы снова будете реализовывать мемоизирующий декоратор "memoizing".
Но на этот раз декоратор должен принимать аргумент, задающий максимальное
количество запоминаемых значений.
При превышении количества запомненных значений лишние должны быть отброшены,
причём сначала — самые старые!

Напоминаю, мемоизируемые функции считать численными функциями одного аргумента.
И не забудьте про functools.wraps!
"""
from functools import wraps


def memoizing_mine(max_memory_size):
    def wrapper(function):
        memory = {}
        history = []
        @wraps(function)
        def inner(argument):
            memoized_result = memory.get(argument)
            # by default get returns None when there's no such key
            # you can also specify default value as a second parameter
            if memoized_result is None:
                memoized_result = function(argument)
                history.append(argument)
                memory[argument] = memoized_result
            if len(memory) > max_memory_size:  # should be nested
                old = history.pop(0)
                memory.pop(old)
            return memoized_result
        return inner
    return wrapper


def memoizing(limit):
    """
    Make decorator that will remember recent results of function (up to limit).

    Arguments:
        limit, maximum number of results to remember

    Returns:
        memoizing decorator

    """
    def wrapper(function):
        """
        Memoize function.

        Arguments:
            function, it will be memoized

        Returns:
            memoized version of function

        """
        memory = {}
        order = []
        @wraps(function)
        def inner(argument):
            memoized_result = memory.get(argument)
            if memoized_result is None:
                memoized_result = function(argument)
                memory[argument] = memoized_result
                order.append(argument)
                if len(order) > limit:
                    oldest_argument = order.pop(0)
                    memory.pop(oldest_argument)
            return memoized_result
        return inner
    return wrapper


@memoizing(3)
def f(x):
    print('Calculating...')
    return x * 10


print(f(1))
print(f(1))  # будет "вспомнено"
print(f(2))
print(f(3))
print(f(4))  # вытеснит запомненный результат для "1"
print(f(1))  # будет перевычислено
