"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def main():
    answer = ""

    while answer != "y":
        answer = input("Bored? (y/n) ").lower()

    print("Well, let's stop this, then.")


if __name__ == "__main__":
    main()
