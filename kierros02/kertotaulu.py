"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""

COUNT = 10


def main():

    try:
        number = int(input("Choose a number: "))
    except ValueError:
        print("Bad input!")
        return

    counter = 1

    while counter <= COUNT:

        print(f"{counter} * {number} = {counter*number}")
        counter += 1


if __name__ == "__main__":
    main()
