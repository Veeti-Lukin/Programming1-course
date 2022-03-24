"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
from math import factorial


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


def probability_calculator(total, drawn):
    """
    calculates probability for one row to win the jackpot
    :param total: int, total number of balls
    :param drawn: int, amount of drawn balls
    :return: int, total number of rows
    """
    return int(factorial(total) / (factorial((total-drawn)) * factorial(drawn)))


def main():

    amount_of_balls = number_input_manager("Enter the total number of lottery balls: ")
    amount_of_drawn = number_input_manager("Enter the number of the drawn balls: ")

    if amount_of_drawn < 0 or amount_of_balls < 0:
        print("The number of balls must be a positive number.")

    elif amount_of_drawn > amount_of_balls:
        print("At most the total number of balls can be drawn.")

    else:
        print(f"The probability of guessing all {amount_of_drawn} balls correctly "
              f"is 1/{probability_calculator(amount_of_balls, amount_of_drawn)}")


if __name__ == "__main__":
    main()
