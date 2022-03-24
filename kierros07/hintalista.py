"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():

    while True:
        user_input = input("Enter product name: ").strip().lower()
        # program stops if user doesn't write anything
        if user_input == "":
            print("Bye!")
            break

        if user_input in PRICES:
            print(f"The price of {user_input} is {PRICES[user_input]:.2f} e")
        else:
            print(f"Error: {user_input} is unknown.")


if __name__ == "__main__":
    main()
