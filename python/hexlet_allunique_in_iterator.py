def all_unique_mine(iterat):
    uniques = set()
    length = 0
    for item in iterat:
        uniques.update({item})
        length += 1
    return len(uniques) == length

def all_unique(iterable):
    items = list(iterable)
    return len(items) == len(set(items))

print(all_unique('cat'))
print(all_unique([1, 2, 1]))