
def level1(level1arg):
    print('what was passed to level1 function:', level1arg)
    def inner(level2arg):
        print('what was passed to level2(inner) function:', level2arg)
    return inner
level1('for level1')('for level2')





#*args
#args - it's a tuple
#*args - it's first element because tuple gets unpacked