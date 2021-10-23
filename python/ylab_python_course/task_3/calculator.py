"""A CLI script to calculate values for geometric shapes."""
from inspect import signature

from shapes import SHAPES

SEPARATOR = "\n\n"


def print_separator():
    """Print a separator between console output blocks."""
    print(SEPARATOR)


while True:

    # display all shapes
    for number, shape in SHAPES.items():
        print(f"{number}. {shape.__name__}")

    # ask to choose shape
    try:
        shape_number = int(input("Choose shape: "))
        shape_class = SHAPES[shape_number]
    except (ValueError, KeyError):
        print("Error: unknown shape.")
        continue

    # display all parameters
    print_separator()
    print(shape_class.__init__.__doc__)

    # ask to input each argument one by one
    shape_parameters = signature(shape_class.__init__).parameters
    number_of_args = len(shape_parameters) - 1  # exclude 'self'
    args = []
    for i in range(0, number_of_args):
        try:
            args.append(float(input(f"Input argument {i + 1}: ")))
        except (ValueError):
            print("Error: invalid argument.")
            continue

    try:
        user_shape = shape_class(*args)
    except ValueError as e:
        print(f"Error: {e}")
        print_separator()
        continue

    # display docstrings of calculation methods
    print_separator()
    method_names = [
        method for method in dir(user_shape) if method.startswith("get") is True
    ]
    enumerated_method_names = {
        index: method_name for (index, method_name) in enumerate(method_names, start=1)
    }
    for number, method_name in enumerated_method_names.items():
        print(f"{number}. ", end="")
        print(eval(f"user_shape.{method_name}.__doc__"))

    # ask to choose one method
    try:
        method_number = int(input("Choose an action: "))
        user_method = enumerated_method_names[method_number]
    except (ValueError, KeyError):
        print("Error: unknown method.")
        print("\n\n")
        continue
    print(eval(f"user_shape.{user_method}()"))

    quit()
