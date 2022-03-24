"""
COMP.CS.100 tilastointia.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Description of the program:
Takes numbers as an input data.
Calculates mean and standard deviation of those numbers.
Makes a histogram of the data
"""
from math import sqrt


def gather_inputs():
    """
    Gathers user inputs inside a list. Gathering stops if a blank line is given
    Checks if input was a number, prints error if not

    :return: list, list of user inputted numbers
    """
    list_of_inputs = []

    while True:
        user_input = input()

        # input gathering stops to a blank line
        if user_input == "":
            break

        try:
            user_input = float(user_input)
            list_of_inputs.append(user_input)
        except ValueError:
            # input wasn't a number
            print("Bad input")

    return list_of_inputs


def calculate_mean(given_list):
    """
    Calculates mean value of elements in a list.
    Assumes that elements are numbers

    :param given_list: list
    :return: int, mean value of elements
    """

    return sum(given_list) / len(given_list)


def calculate_std_dev(given_list, mean):
    """
    Calculates std deviation value of elements in a list, by first calculating
    variance and then taking square root of variance
    Assumes that elements are numbers

    :param given_list: list
    :param mean: float, mean of lists elements
    :return: float, variance value of elements
    """
    total = 0

    for value in given_list:
        total += (value-mean)**2

    return sqrt(1 / (len(given_list) - 1) * total)


def print_histogram(std_dev, given_list, mean):
    """
    Makes a category histogram of a list with six categories.
    Category boundaries are defined like this:
    0.0–0.5*σ
    0.5*σ–1.0*σ
    1.0*σ–1.5*σ             σ = standard deviation
    1.5*σ–2.0*σ
    2.0*σ–2.5*σ
    2.5*σ–3.0*σ
    Values are placed in categories by fist taking out the mean
    and changing that to absolute value, then checking which category
    value should be placed to.
    Assumes that list elements are numbers.

    :param std_dev: float, standard deviation of list elements
    :param given_list: list
    :param mean: float, mean of list elements
    :return: None
    """
    mark = "*"

    for category_number in range(0, 6):
        lower_boundary = category_number * 0.5 * std_dev
        upper_boundary = (category_number + 1) * 0.5 * std_dev
        values_inside_boundaries = 0

        for value in given_list:
            value_after_calculations = abs(value - mean)

            if lower_boundary <= value_after_calculations < upper_boundary:
                values_inside_boundaries += 1

        print(f"Values between std. dev. "
              f"{lower_boundary:.2f}-{upper_boundary:.2f}: "
              f"{values_inside_boundaries * mark}")


def main():
    print("Enter the data, one value per line.")
    print("End by entering empty line.")
    list_of_numbers = gather_inputs()

    # program stops if there is not enough data in the list
    if len(list_of_numbers) < 2:
        print("Error: needs two or more values.")
        return

    mean_value = calculate_mean(list_of_numbers)
    std_dev = calculate_std_dev(list_of_numbers, mean_value)

    print(f"The mean of given data was: {mean_value:.2f}")
    print(f"The standard deviation of given data was: {std_dev:.2f}")

    # if standard deviation is 0 no histogram is printed
    if std_dev == 0:
        print("Deviation is zero.")
        return

    print_histogram(std_dev, list_of_numbers, mean_value)


if __name__ == "__main__":
    main()
