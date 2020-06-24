from typing import List


def find_index_of_smallest(list: List) -> int:
    index_smallest = 0
    for i, item in enumerate(list):
        if item < list[index_smallest]:
            index_smallest = i
    return index_smallest


def sort_list(list: List) -> List:
    for i in range(len(list)):


print(find_index_of_smallest([1, 0, -300, 4, -500]))