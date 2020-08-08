def greet(name, surname):
    return 'Hello, {name} {surname}!'.format(name=name, surname=surname)


def partial_apply(function, first_arg):
    """
    partial_apply принимает функцию от двух аргументов и первый аргумент, 
    а возвращает замыкание — функцию, которая примет второй аргумент 
    и наконец применит замкнутую функцию к обоим аргументам 
    (и вернёт результат
    """
    def inner(second_arg):
        return function(first_arg, second_arg)
    return inner

def flip(two_arg_function):
    """
    Функция flip принимает в качестве единственного аргумента функцию от двух 
    аргументов. Возвращаемое замыкание должно также принять два аргумента, 
    а затем применить к ним замкнутую функцию, но аргументы подставить 
    в обратном порядке. Таким образом flip как бы "переворачивает" ("flips") 
    исходную функцию.
    """
    def inner(first_arg, second_arg):
        return two_arg_function(second_arg, first_arg)
    return inner


f = partial_apply(greet, 'Dorian')
print(f('Grey'))

ff = flip(greet)
print(ff('Christian', 'Teodor'))