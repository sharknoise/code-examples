from typing import List


def quicksort(numbers: List[int]) -> List[int]:
    if len(numbers) < 2:
        return numbers
    else:
        pivot = numbers[0]
        lesser_items = [i for i in numbers[1:] if i <= pivot]
        greater_items = [i for i in numbers[1:] if i > pivot]
        return quicksort(lesser_items) + [pivot] + quicksort(greater_items)


print(quicksort([2, 7, 8, 3, -45]))
