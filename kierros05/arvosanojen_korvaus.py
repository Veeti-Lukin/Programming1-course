"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def convert_grades(given_list):
    """
    changes all the elements that are greater than 0 to 6
    :param given_list: list
    :return: None
    """
    for count, value in enumerate(given_list):
        if value > 0:
            given_list[count] = 6


def main():
    pass


if __name__ == "__main__":
    main()
