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


def input_to_list(amount_of_elements):
    """
    adds changeable amount of numbers to a list and returns it
    :param amount_of_elements: int, how many elements to add
    :return: list
    """
    list_of_values = []

    print(f"Enter {amount_of_elements} numbers:")

    for i in range(amount_of_elements):
        number = number_input_manager("")
        list_of_values.append(number)

    return list_of_values


def main():

    amount_of_values = number_input_manager(
        "How many numbers do you want to process: ", allow_negative=False)

    asd_list = input_to_list(amount_of_values)

    searched_number = number_input_manager("Enter the number to be searched: ")

    if searched_number in asd_list:
        print(f"{searched_number} shows up "
              f"{asd_list.count(searched_number)} times among the numbers you have entered.")

    else:
        print(f"{searched_number} is not among the numbers you have entered.")


if __name__ == "__main__":
    main()
