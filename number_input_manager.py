"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def number_input_manager(string="", float_or_int=float, allow_negative=True):
    """
    Asks input from user with changeable question
    and checks if input is an positive number.

    :param allow_negative: bool, if negative values are allowed or not
    :param string: str, question asked inside input function
    :param float_or_int: bool, changes if return value should be int or float
    :return: int or float , user input if it was a number
    """

    while True:
        answer = input(string)
        try:
            answer = float_or_int(answer)

            if not allow_negative:
                # if positive
                if answer >= 0:
                    # input was an positive number so we return it
                    return answer
                    # break
                else:
                    print("Input can not be negative")

            else:
                return answer

        except ValueError:
            print("Bad input")  # input wasn't a number


def main():
    pass


if __name__ == "__main__":
    main()
