import operator
import functools


def keep_truthful(iterable):
    return filter(operator.truth, iterable)


def abs_sum(numbers) -> int:
    return sum(map(abs, numbers))


def walk(dictionary: dict, iterable_path):
    return functools.reduce(operator.getitem, iterable_path, dictionary)


print(list(keep_truthful([True, False, "", "foo"])))

print(abs_sum([-3,7,-8]))

print(walk({'a': {7: {'b': 42}}}, ["a", 7, "b"]))