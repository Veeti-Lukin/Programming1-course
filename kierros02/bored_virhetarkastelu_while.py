"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
ALLOWED_CHARACTERS = ("Y", "y", "N", "n")

def main():

    answer = ""

    while answer.upper() != "Y":
        invalid_input = True

        while invalid_input:
            answer = input("Bored? (y/n) ")

            if answer in ALLOWED_CHARACTERS:
                invalid_input = False
            else:
                print("Incorrect entry.")

    print("Well, let's stop this, then.")


if __name__ == "__main__":
    main()
