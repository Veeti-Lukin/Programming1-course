"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""

STRING = "A suitable smiley would be"
smiles = [":'(", ":-(", ":-|", ":-)", ":-D"]


def main():
    mood = input("How do you feel? (1-10) ")

    try:
        mood = int(mood)
    except ValueError:
        print("Bad input!")
        return

    if 1 <= mood <= 10:
        if mood == 1:   # mood = 1
            print(STRING, smiles[0])
        elif mood < 4:  # mood = 2-3
            print(STRING, smiles[1])
        elif mood < 8:  # mood = 4-7
            print(STRING, smiles[2])
        elif mood < 10:  # mood = 8-9
            print(STRING, smiles[3])
        else:            # mood = 10
            print(STRING, smiles[4])
    else:
        print("Bad input!")


if __name__ == "__main__":
    main()
