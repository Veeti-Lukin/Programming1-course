"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def number_input_manager(string="", float_or_int=int, allow_negative=False):
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


def gather_lines():
    """
    gaters user inputs to a list
    :return: list
    """
    lines = []

    while True:
        answer = input()
        if answer == "":
            break
        parts = answer.split()

        for split in parts:
            lines.append(split)

    return lines


def main():
    print("Enter text rows. Quit by entering an empty row.")
    data = gather_lines()
    characters_per_line = number_input_manager(
        "Enter the number of characters per line: ")
    index = 0
    line_as_list = []

    while index < len(data):
        line_as_list = []
        try:
            while len(" ".join(
                    line_as_list + [data[index]])) <= characters_per_line:
                line_as_list.append(data[index])
                index += 1
        except IndexError:
            line_as_text = " ".join(line_as_list)
            print(line_as_text)
            return

        how_how_many_spaces = characters_per_line % len(" ".join(line_as_list))

        len(line_as_list)

        for i in range(1, how_how_many_spaces * 2, 2):
            if i >= len(line_as_list):
                i = (i - len(line_as_list) + 1) * 2
            line_as_list.insert(i, "")



        line_as_text = " ".join(line_as_list)
        print(line_as_text)


if __name__ == "__main__":
    main()
