def diff_keys1(old_dict, new_dict) -> dict:
    old_key_set = set(old_dict.keys())
    new_key_set = set(new_dict.keys())
    kept = old_key_set & new_key_set
    added = new_key_set - old_key_set
    removed = old_key_set - new_key_set
    return {'kept': kept, 'added': added, 'removed': removed}


def diff_keys2(old, new):
    old_keys = set(old.keys())
    new_keys = set(new.keys())
    return {
        'kept': old_keys & new_keys,
        'added': new_keys - old_keys,
        'removed': old_keys - new_keys,
    }