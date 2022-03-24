"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
ZIP = 3
BOING = 7
# zip boing when both zip and boing


def main():
    try:
        count = int(input("How many numbers would you like to have? "))

        for i in range(1, count+1):

            if i % ZIP == 0 and i % BOING == 0:
                print("zip boing")

            elif i % BOING == 0:
                print("boing")

            elif i % ZIP == 0:
                print("zip")

            else:
                print(i)

    except ValueError:
        print("Bad input!")


if __name__ == "__main__":
    main()
