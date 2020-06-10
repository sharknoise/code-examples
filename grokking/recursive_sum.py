from typing import List


def rec_sum(numbers: List) -> int:
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + rec_sum(numbers[1:])


def rec_sum2(numbers: List) -> int:
    if numbers == []:
        return 0
    else:
        return numbers[0] + rec_sum(numbers[1:])


print(rec_sum([1, 2, 3, -3]))

print(rec_sum2([1, 2, 3, -3]))
