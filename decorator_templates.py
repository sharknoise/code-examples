def decorator(function):
    def inner(*args, **kwargs):
        result = function(*args, **kwargs)
        print('result =', result)
        return result
    return inner

def decorator0(decorator0_setting):
    def wrapper(function):
        def inner(*args, **kwargs):  # decorated function_parameters
            print(decorator0_setting)
            return function(*args, **kwargs)
        return inner
    return wrapper


def decorator1(decorator1_setting):
    print('1')
    print(decorator1_setting)
    def wrapper(function):
        print('5')
        def inner(*args, **kwargs):  # decorated function_parameters
            print(decorator1_setting)
            kwargs['to_next_decorator'] = 'message from decorator1'
            return function(*args, **kwargs)
        print('6')
        return inner
    return wrapper


def decorator2(decorator2_setting):
    print('2')
    def wrapper(function):
        print('3')
        def inner(*args, **kwargs):  # decorated function_parameters
            print(decorator2_setting)
            print(kwargs.pop('to_next_decorator'))
            return function(*args, **kwargs)
        print('4')
        return inner
    return wrapper

#@decorator
@decorator1('setting1')
@decorator2('setting2')
def printer(text: str):
    print(text)

printer('function text')

"""
декоратор как бы дополняет функцию - к ее коду добавляется содержимое inner
чтобы выполнился сам код функции делается return

можно не принимать *args и **kwargs, а потом вернуть только function без параметров, 
если сам ее код не будет выполняться (как в hexlet interactive functions)

Decorators are called at start time (when the python interpreter reads the code as the program starts), not at runtime (when the decorated function is actually called).
At runtime, it is the wrapped function wrapper which is called and which itself calls the decorated function and returns its result.
So this is totally normal that the print line gets executed.
Move the print inside wrapper and this won't happen anymore.

порядок выполнения
##### "start time"
1
2
3
4
5
6
##### runtime
setting1
setting2
function text
"""