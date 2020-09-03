class Foo(object):
    def __bool__(self):
        return False

    def __len__(self):
        return 9001


bar = Foo()
print(bool(bar))
print(len(bar))
