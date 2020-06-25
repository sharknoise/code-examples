"""
В этом задании под деревом понимается любой список элементов, 
которые в свою очередь могут быть также деревьями (списками). Пример:

[
  3, # лист
  [5, 3], # узел
  [[2]] # узел
]

Реализуйте функцию, которая принимает на вход дерево, и возвращает новое, 
элементами которого являются дети вложенных узлов.

Пример

>>> from solution import remove_first_level
>>>
>>> tree1 = [[5], 1, [3, 4]]
>>> remove_first_level(tree1)
[5, 3, 4]
>>> tree2 = [1, 2, [3, 5], [[4, 3], 2]]
>>> remove_first_level(tree2)
[3, 5, [4, 3], 2]
>>>
"""

import itertools


def remove_first_level_via_loop(tree: list) -> list:
    flattened = []
    for item in tree:
        if isinstance(item, list):
            flattened.extend(item)
    return flattened


def remove_first_level(tree):
    children = filter(lambda item: isinstance(item, list), tree)
    return list(itertools.chain(*children))


tree1 = [[5], 1, [3, 4]]
print(remove_first_level(tree1))
tree2 = [1, 2, [3, 5], [[4, 3], 2]]
print(remove_first_level(tree2))
