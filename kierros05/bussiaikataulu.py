"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
BUSSES = [630, 1015, 1415, 1620, 1720, 2000]


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


def find_right_index(time, timetable=BUSSES):
    """
    finds a right spot where we start printing the values
    :param time: int, time now
    :param timetable: list, list of times when busses leave
    :return:
    """
    for index, value in enumerate(timetable):
        if value >= time:
            right_index = index
            return right_index

    return 0  # no more busses today


def main():
    time = number_input_manager("Enter the time (as an integer): ")
    list_index = find_right_index(time)

    count = 3

    print("The next buses leave:")
    while count != 0:

        try:
            print(BUSSES[list_index])
            count -= 1
            list_index += 1

        except IndexError:
            list_index = 0

if __name__ == "__main__":
    main()
