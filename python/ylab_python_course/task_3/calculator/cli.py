"""Functions for the CLI geometric caclulator."""
from inspect import signature
from typing import Type

from calculator.shapes import SHAPES, Shape

SEPARATOR = "\n\n"


def print_separator():
    """Print a separator between console output blocks."""
    print(SEPARATOR)


def ask_shape_class() -> Type[Shape]:
    """Display all shapes, ask the user to choose one, return it."""
    for number, shape in SHAPES.items():
        print(f"{number}. {shape.__name__}")
    shape_number = int(input("Choose shape: "))
    return SHAPES[shape_number]


def ask_shape_arguments(shape_class: Type[Shape]) -> list:
    """Ask for arguments to create a shape object.

    Display the initial Shape parameters, ask the user to input
    them one by one. Return the choice.
    """
    print(shape_class.__init__.__doc__)

    shape_parameters = signature(shape_class.__init__).parameters
    number_of_args = len(shape_parameters) - 1  # exclude 'self'
    args = []
    for i in range(0, number_of_args):
        args.append(float(input(f"Input argument {i + 1}: ")))
    return args


def ask_method_name(shape: Shape) -> str:
    """Ask for calculation method.

    Display the docstrings of Shape's calculation methods.
    Ask to choose one, return it.
    """
    method_names = [
        method for method in dir(shape) if method.startswith("get") is True
    ]
    enumerated_method_names = {
        index: method_name
        for (index, method_name) in enumerate(method_names, start=1)
    }
    for number, method_name in enumerated_method_names.items():
        print(f"{number}. ", end="")
        print(eval(f"shape.{method_name}.__doc__"))

    method_number = int(input("Choose a calculation: "))
    return enumerated_method_names[method_number]
