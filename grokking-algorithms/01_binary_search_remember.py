def binary_search(list, item):
    low_index = 0
    high_index = len(list) - 1
    while low_index <= high_index:
        index_guess = (low_index + high_index) // 2
        if list[index_guess] == item:
            return index_guess
        elif list[index_guess] > item:
            high_index = index_guess - 1
        elif list[index_guess] < item:
            low_index = index_guess + 1
    return None


sorted_list = [3, 6, 8, 10]
print(binary_search(sorted_list, 10))
