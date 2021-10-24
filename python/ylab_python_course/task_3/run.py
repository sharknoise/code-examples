"""A CLI script to calculate values for geometric shapes."""
import calculator.cli as cli

user_shape_class, user_shape, user_method_name = None, None, None

while user_shape_class is None:
    try:
        user_shape_class = cli.ask_shape_class()
    except (ValueError, KeyError):
        print("Error: unknown shape.")

cli.print_separator()

while user_shape is None:
    try:
        user_arguments = cli.ask_shape_arguments(user_shape_class)
    except (ValueError):
        print("Error: invalid argument.")
        continue
    try:
        user_shape = user_shape_class(*user_arguments)
    except ValueError as e:
        print(f"Error: {e}")

cli.print_separator()

while user_method_name is None:
    try:
        user_method_name = cli.ask_method_name(user_shape)
    except (ValueError, KeyError):
        print("Error: unknown calculation.")

cli.print_separator()

print(eval(f"user_shape.{user_method_name}()"))
quit()
