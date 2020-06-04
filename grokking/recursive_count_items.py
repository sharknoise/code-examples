from typing import List

def count_items(numbers: List) -> int:
    if numbers == []:
        return 0
    #else:
    #    return 1 + count_items(numbers[1:])
    return 1 + count_items(numbers[1:])

print(count_items([1, 2]))        
