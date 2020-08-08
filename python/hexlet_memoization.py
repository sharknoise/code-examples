"""
реализовать декоратор, добавляющий функции мемоизацию.
Мемоизация — это запоминание уже вычисленных результатов, для уже однажды
встреченных аргументов.

Для простоты будем считать, что мемоизироваться будут численные функции
одного аргумента (аргумент — число, результат — тоже число).

@memoized
.. def f(x):
..     print('Calculating...')
..     return x * 10
...
>> f(1)
Calculating...
10
>> f(1)
10
"""


def memoized_mine(function):
    memoized_calls = {}

    def inner(arg):
        if arg in memoized_calls:
            return memoized_calls[arg]
        result = function(arg)
        memoized_calls[arg] = result
        return result
    return inner


def memoized(function):
    memory = {}

    def inner(argument):
        memoized_result = memory.get(argument)
        # by default get returns None when there's no such key
        # you can also specify default value as a second parameter
        if memoized_result is None:
            memoized_result = function(argument)
            memory[argument] = memoized_result
        return memoized_result

    return inner


@memoized
def f(x):
    print('Calculating...')
    return x * 10


print(f(1))
print(f(1))
print(f(42))
print(f(42))
