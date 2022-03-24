"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
ALLOWED_CHARS = ("Y", "N", "y", "n")


def main():

    invalid_input = True

    while invalid_input:

        answer = input("Answer Y or N: ")

        if answer in ALLOWED_CHARS:
            invalid_input = False

        else:
            print("Incorrect entry.")

    print(f"You answered {answer}")


if __name__ == "__main__":
    main()
