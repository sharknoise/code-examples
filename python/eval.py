nests = [1, 2, [11, 12]]
code = 'nests[2].append(x)'
x = 13
eval(code)
print(nests)
