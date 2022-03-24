"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def payload(key):
    """
    return value for <key> from PRICES dict
    :param key: str, dict key
    :return: float, dict value
    """
    return PRICES[key]


def main():

    for item in sorted(PRICES, key=payload):
        print(f"{item} {PRICES[item]:.2f}")


if __name__ == "__main__":
    main()
