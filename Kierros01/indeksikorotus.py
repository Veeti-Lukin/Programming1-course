"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
INDEX_RAISE = 1.17


def main():
    amount = input("Enter the amount of the study benefits: ")
    raised_amount = float(amount) * (INDEX_RAISE/100 +1)

    print(f"If the index raise is {INDEX_RAISE} percent, the study benefit,\n"
    f"after a raise, would be {raised_amount} euros")

    raised_amount = raised_amount * (INDEX_RAISE/100 +1)
    print(f"and if there was another index raise, the study\n"
          f"benefits would be as much as {raised_amount} euros")

if __name__ == "__main__":
    main()
