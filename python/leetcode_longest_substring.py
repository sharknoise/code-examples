"""https://leetcode.com/problems/longest-substring-without-repeating-characters/"""


def longest_substring_length(string: str) -> int:
    substring_lengths = [0]
    for index, _ in enumerate(string):
        remaining_slice = string[index:]
        temp_unique_chars = set()
        for remaining_char in remaining_slice:
            if remaining_char in temp_unique_chars:
                break
            else:
                temp_unique_chars.add(remaining_char)
        substring_lengths.append(len(temp_unique_chars))
    return max(substring_lengths)


print(longest_substring_length('abcabcbb'))  # => 3
print(longest_substring_length('bbbbb'))     # => 1
print(longest_substring_length('pwwkew'))    # => 3
print(longest_substring_length(''))          # => 0
print(longest_substring_length(' '))         # => 1
print(longest_substring_length('a'))         # => 1