import re


def check(string):
    return re.match(r'\boo', string)


first_string = 'oodar'
second_string = 'boodan'

print(check(first_string))
print(check(second_string))
