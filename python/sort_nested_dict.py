def sort_dict(dictionary):
    """Sort all levels of a nested dict by key (alphabetically)."""
    results = {}
    for key, value in sorted(dictionary.items()):
        if isinstance(value, dict):
            results[key] = sort_dict(value)
        else:
            results[key] = value
    return results
