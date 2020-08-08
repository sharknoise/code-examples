def simple_input(_, prompt):                                                    #1
    """Just input string."""
    return input(prompt)  # noqa: S322, WPS421


def asks(name, prompt):                                                         #2  #10 #14
    """
    Описывает один запрос аргумента.

    Arguments:
        name - имя аргумента оборачиваемой функции,

        prompt - текст приглашения.

    Returns:
        декоратор, который и обернёт нужную функцию. Помните, после
        описания всех аргументов нужно результат обернуть в
        декоратор interactive! 
        [question приделываются к функции (calc) когда интерпретатор приделывает декораторы в "start time."]
        [во время запуска calc этот декоратор вообще не читается, поэтому у него нет inner]

    """
    # BEGIN (write your solution here)
    def wrapper(function): #принимает calc                                       #11 #15(ближний к кальк)
        function.questions = (
            (name, prompt), # вставляется в начало questions чтобы соблюдался порядок
        ) + getattr(function, 'questions', ())
        return function
    return wrapper                                                               #12
    # END


def interactive(                                                                 #4 #6
    description,
    input_function=simple_input,
    output_function=print,  # noqa: T002                                         #3
):
    """
    Делает функцию с описанными параметрами интерактивной.

    Интерактивной может быть функция без параметров. В этом случае декоратор
    asks не потребуется.

    Arguments:
        description - описание, которое будет выведено в начале
        диалога (интерактивной сессии).

        input_function - функция, принимающая имя аргумента и приглашение,
        и возвращающая введённый пользователем текст (str).

        output_function - функция, которая будет использована для вывода
        описания и результата вызова оборачиваемой функции.

    Returns:
        декоратор, который обернёт целевую функцию.

    """
    # BEGIN (write your solution here)
    def wrapper(function):# принимает модифицированный calc после декораторов       #7
        def inner():
            questions = getattr(function, 'questions', ())
            output_function(description)
            kwargs = {}
            for argument, prompt in questions:
                kwargs[argument] = input_function(argument, prompt)
            return output_function(
                function(**kwargs),
            )
        return inner
    return wrapper                                                                   #8
    # END


@interactive('Calculator')                                                           #5
@asks('x', 'Enter first number: ')                                                    #9
@asks('y', 'Enter second number: ')                                                     #13
def calc(x, y):
    return int(x) + int(y)


if __name__ == '__main__':
    calc()
