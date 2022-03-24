"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def read_input(string):
    """
    Asks input from user with changeable question and checks if input is an positive number.

    :param string: str, question asked inside input function
    :param float_or_int: bool, changes if return value should be int or float
    :return: int, user input if it was an int
    """

    while True:
        answer = input(string)
        try:
            answer = int(answer)

            if answer > 0:  # if positive
                return answer  # input was an positive number so we return it
                # break

            else:
                pass

        except ValueError:
            continue  # input wasn't a number


def print_box(w, h, m):
    """
    prints a box
    :param w: str, width of the box
    :param h: str, height of the box
    :param m: str, mark used to print the box
    :return: None
    """
    w = int(w)
    h = int(h)
    for height in range(0, h):
        for width in range(0, w):
            print(m, end="")
        print()


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)

if __name__ == "__main__":
    main()
