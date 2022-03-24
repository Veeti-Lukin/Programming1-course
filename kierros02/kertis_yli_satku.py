"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""

COUNT = 100


def main():

    try:
        number = int(input("Choose a number: "))
    except ValueError:
        print("Bad input!")
        return

    counter = 1
    sum = 0

    while sum <= 100:
        sum = counter * number
        print(counter, "*", number, "=", sum)
        counter += 1


if __name__ == "__main__":
    main()
