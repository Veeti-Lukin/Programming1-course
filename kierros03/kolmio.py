"""
Ohjelmointi 1 / Programming 1
Trangle's Area when the Sides Are Known
"""

from math import sqrt


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


def area(side1, side2, side3):
    """

    :param side1: float, first side of the triangle
    :param side2: float, second side of the triangle
    :param side3: float, third side of the triangle
    :return: float, area of the triangle
    """
    s = (side1 + side2 + side3) * 1/2
    area = sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return area


def main():
    line1 = number_input_manager("Enter the length of the first side: ")
    line2 = number_input_manager("Enter the length of the second side: ")
    line3 = number_input_manager("Enter the length of the third side: ")

    print(f"The triangle's area is {area(line1, line2, line3):.1f}")


if __name__ == "__main__":
    main()
