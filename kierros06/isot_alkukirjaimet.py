"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def capitalize_initial_letters(text):
    """
    takes text as input changes first letter of every word to capital letter
    :param text: str
    :return: str
    """
    parts = text.split()

    for i in range(0, len(parts)):
        parts[i] = parts[i].capitalize()

    return " ".join(parts)


def main():
    while True:
        print(capitalize_initial_letters(input()))


if __name__ == "__main__":
    main()
