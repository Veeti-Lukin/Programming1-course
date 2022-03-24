"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def number_input_manager(string, float_or_int=int, allow_negative=True):
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


def main():
    list_of_values = []

    print("Give 5 numbers:")
    for i in range(5):
        number = number_input_manager("Next number: ")
        list_of_values.append(number)

    print("The numbers you entered, in reverse order:")

    for value in reversed(list_of_values):
        print(value)


if __name__ == "__main__":
    main()
