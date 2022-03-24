"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def number_input_manager(string, float_or_int=int, allow_negative=False):
    """
    Asks input from user with changeable question and checks if input is an positive number.

    :param allow_negative: bool, if negative values are allowed or not
    :param string: str, question asked inside input function
    :param float_or_int: bool, changes if return value should be int or float
    :return: int, user input if it was an int
    """

    while True:
        answer = input(string)
        try:
            answer = float_or_int(answer)

            if not allow_negative:

                if answer >= 0:  # if positive
                    return answer  # input was an positive number so we return it
                    # break
                else:
                    print("Input can not be negative")

            else:
                return answer

        except ValueError:
            print("Bad input")  # input wasn't a number


def print_box(width, height, border_mark="#", inner_mark=" "):
    """
    prints box
    :param width: int, width
    :param height: int, height
    :param border_mark: str, line drawing mark
    :param inner_mark: str, inner mark
    :return: None
    """
    for i in range(height):
        for j in range(width):

            if i == 0 or i == height-1:
                print(border_mark, end="")

            else:
                if j == 0 or j == width-1:
                    print(border_mark, end="")
                else:
                    print(inner_mark, end="")
        print()
    print()


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
