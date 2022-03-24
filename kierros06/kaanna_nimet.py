"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def reverse_name(name):
    """
    reverses name
    :param name: str
    :return:
    """

    names_list = name.strip().split(",")
    names_list.reverse()
    return " ".join(names_list).strip()

def main():
    while True:
        print(reverse_name(input()))


if __name__ == "__main__":
    main()
