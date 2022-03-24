"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
EPSILON = 0.000000001


def number_input_manager(string, float_or_int=float):
    """
    Asks input from user with changeable question and checks if input is an positive number.

    :param string: str, question asked inside input function
    :param float_or_int: bool, changes if return value should be int or float
    :return: int, user input if it was an int
    """

    while True:
        answer = input(string)
        try:
            answer = float_or_int(answer)

            if answer >= 0:  # if positive
                return answer  # input was an positive number so we return it
                # break

            else:
                print("Input can not be negative")

        except ValueError:
            print("Bad input")  # input wasn't a number


def compare_floats(float_value1, float_value2, epsilon):
    """
    checjks if 2 flaots are close enogh of each other to be considered same
    :param float_value1: float
    :param float_value2: float
    :param epsilon: marginal of error
    :return: bool
    """
    return abs(float_value1 - float_value2) < epsilon


def main():
    while True:
        print(compare_floats(number_input_manager("first value:"),
                             number_input_manager("second value:"), EPSILON))


if __name__ == "__main__":
    main()
