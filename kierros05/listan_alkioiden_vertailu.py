"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""

def are_all_members_same(list_to_test):
    """
    finds out if all the elements of list are identical
    :param list_to_test: list
    :return: bool
    """
    return len(set(list_to_test)) <= 1

def main():
    pass


if __name__ == "__main__":
    main()
