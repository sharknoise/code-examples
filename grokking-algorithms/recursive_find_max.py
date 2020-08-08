def find_max(numbers: List) -> int:
    if len(numbers) == 2:
        return numbers[0] if numbers[0] > numbers [1] else numbers [1]
    sub_max = find_max(numbers[1:])
    return numbers[0] if numbers[0] > sub_max else sub_max

print(find_max([5,2,7,11,3,10]))