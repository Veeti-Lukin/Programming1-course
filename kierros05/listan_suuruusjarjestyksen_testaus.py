"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def is_the_list_in_order(given_list):
    """
    checks if the list elements are inorder or not
    :param given_list: list
    :return: bool,
    """
    return given_list == sorted(given_list)


def main():
    pass


if __name__ == "__main__":
    main()
