"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def main():

    a = 0
    b = 0
    c = 1

    try:
        count = int(input("How many Fibonacci numbers do you want? "))

        for i in range(1, count+1):
            print(f"{i}. {c}")

            a = b
            b = c
            c = a + b

    except ValueError:
        print("Bad input!")


if __name__ == "__main__":
    main()
