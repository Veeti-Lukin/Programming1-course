"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def create_an_acronym(name):
    """
    smart function to create acronym
    :param name: str, name
    :return: str, acronym of the name
    """
    parts = name.split()
    acronym = ""
    for part in parts:
        acronym += part[0].upper()

    return acronym


def main():
    while True:
        print(create_an_acronym(input()))


if __name__ == "__main__":
    main()
