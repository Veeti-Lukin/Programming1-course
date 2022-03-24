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


def make_list(string, amount=5):
    """
    makes a list
    :param string: str
    :param amount: int
    :return: list
    """
    list_of_values = []

    for i in range(1, amount+1):
        number = number_input_manager(f"{string} {i}: ", float_or_int=float
                                      , allow_negative=False)
        list_of_values.append(number)

    return list_of_values


def calc_mean(given_list):
    """
    calculates mean value of elements in a list
    :param given_list: list
    :return: int
    """
    total = 0

    for value in given_list:
        total += value

    return total / len(given_list)


def main():
    results = make_list("Enter the time for performance")
    results.remove(max(results))
    results.remove(min(results))

    print(f"The official competition score is {calc_mean(results):.2f} seconds.")


if __name__ == "__main__":
    main()
