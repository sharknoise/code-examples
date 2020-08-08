def filter_map_mine(function, iter_source) -> list:
    results = []
    for item in iter_source:
        condition, result = function(item)
        if condition:
            results.append(result)
    return results

def filter_map(function, items):
    result = []
    for item in items:
        keep, value = function(item)
        if keep:
            result.append(value)
    return result

def make_stars(x):
    if x > 0:
        return True, '*' * x
    return False, ''

for s in filter_map(make_stars, [1, 0, 5, -5, 2]):
    print(s)
