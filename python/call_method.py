class Dog(object):
    def bark(self):
        print('woof!')


rex = Dog()
Dog.bark(rex)  # call through class
rex.bark()  # call through instance
