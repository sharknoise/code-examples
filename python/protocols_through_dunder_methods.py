class TestClass(object):
    def __bool__(self):
        return False

    def __len__(self):
        return 9001


test_instance = TestClass()
print(bool(test_instance))
print(len(test_instance))
