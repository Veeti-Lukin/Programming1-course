"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def main():

    for i in range(1, 11):
        for j in range(1,11):
            print(f"{i*j:4}", end="")
        print()


if __name__ == "__main__":
    main()
