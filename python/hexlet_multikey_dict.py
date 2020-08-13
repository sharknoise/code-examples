"""https://ru.hexlet.io/challenges/python_oop_basics_multikey_dictionary"""


class MultiKeyDict(object):
    """A dictionary with an option of multiple keys for one value."""

    def __init__(self, **kwargs):
        """
        Create a list to store all values and a dict to store all keys.
        The dict structure is {key: int} where the integer references
        a list index.

        Args:
            kwargs: key-value pairs (key1=value1, key2=value2...)
        """
        self._mkd_values = list({**kwargs}.values())
        self._mkd_keys = {}
        temp_keys = list({**kwargs}.keys())
        for temp_key in temp_keys:
            self._mkd_keys[temp_key] = temp_keys.index(temp_key)
        self._mkd_aliases = {}

    def __setitem__(self, key, new_value):
        """
        Change an existing value or add a new key-value pair.

        Args:
            key: key to change or add
            new_value: value to set or add
        """
        if key in self._mkd_keys:
            mkd_index = self._mkd_keys[key]  # noqa: WPS529
            self._mkd_values[mkd_index] = new_value
        else:
            self._mkd_keys[key] = len(self._mkd_values)  # noqa: WPS529
            self._mkd_values.append(new_value)

    def __getitem__(self, key):
        """
        Get a value by its key.

        Args:
            key: key of the required value

        Returns:
            value by the key
        """
        mkd_index = self._mkd_keys[key]
        return self._mkd_values[mkd_index]

    def alias(self, **kwargs):
        """
        Add another key (alias) for the same value.

        Args:
            kwargs: key-alias pair (new_key='old_key')
        """
        new_key = list({**kwargs}.keys())[0]
        old_key = list({**kwargs}.values())[0]
        mkd_index = self._mkd_keys[old_key]
        self._mkd_keys[new_key] = mkd_index

mkd = MultiKeyDict(x=100, y=[10, 20])

mkd.alias(z='x')  # 'z' теперь означает то же, что и 'x'
print(mkd['z'])  # 100

mkd['z'] += 1  # Можно даже менять значение через присваивание,
print(mkd['x'])  # 101

mkd.alias(z='y')  # Теперь 'z' уже равнозначен 'y'
mkd['z'] += [30]
print(mkd['y'])  # [10, 20, 30]
