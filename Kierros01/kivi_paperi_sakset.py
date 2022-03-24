"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def main():
    player1_choice = input("Player 1, enter your choice (R/P/S): ").upper()
    player2_choice = input("Player 2, enter your choice (R/P/S): ").upper()

    if player1_choice != player2_choice:

        if player1_choice == "R" and player2_choice == "S":
            print("Player 1 won!")
        elif player1_choice == "P" and player2_choice == "R":
            print("Player 1 won!")
        elif player1_choice == "S" and player2_choice == "P":
            print("Player 1 won!")
        else:
            print("Player 2 won!")

    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()
