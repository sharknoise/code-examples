def fact (x):
    if x == 1:
        return 1
    else:
        print (x)
        return x * fact(x-1)

print(fact(7))