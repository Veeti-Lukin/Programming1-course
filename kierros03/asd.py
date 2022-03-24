"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def binary_converter(asd):

    asd_len = len(asd)
    sum = 0

    for i in range(0, asd_len):
        xd = int(asd[-(i+1)]) * 2**i
        sum += xd

    return sum


def main():
    while True:
        print(binary_converter(input("Binääri:")))


if __name__ == "__main__":
    main()
