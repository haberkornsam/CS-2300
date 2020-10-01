from Project02.implicit_equation import ImplicitEquation
from Project02.parametric_equation import ParametricEquation

"""
Name: Samuel Haberkorn
Class: CS 2300
Date: 09/30/2020
Assignment: Project 2
"""


FILE = "CS2300P2data"


def main():
    equations = []
    with open(FILE) as file:
        # Read two equations from the file, switching based on the type
        for i in range(2):
            if get_next_char(file) == 'i':
                equations.append(
                    ImplicitEquation(
                        get_float(file), get_float(file), get_float(file),
                        [get_point(file), get_point(file), get_point(file)]
                    )
                )
            else:
                equations.append(
                    ParametricEquation(
                        get_point(file), get_point(file),
                        [get_point(file), get_point(file), get_point(file)]
                    )
                )

    # Iterate over the gathered data and print the summary
    for count, equation in enumerate(equations):
        print(f"Equation {count + 1}")
        print("----------")
        equation.print_summary()
        print("\n\n")


# The three functions below make the reading and parsing of the files easier
def get_point(file) -> (float, float):
    return get_float(file), get_float(file)


def get_float(file) -> float:
    return float(get_next_char(file))


def get_next_char(file, prev_chars=""):
    """
    Recursive function to read in each set of characters.
    If no character or whitespace is read, return the read characters or keep reading (if no characters are read)
    :param file: file
    :param prev_chars: str
    :return: str
    """
    char = file.read(1)

    if not len(char) == 0 and char not in [None, " ", "\n"]:
        return get_next_char(file, prev_chars + char)
    return prev_chars if prev_chars != "" else get_next_char(file)


if __name__ == '__main__':
    main()
