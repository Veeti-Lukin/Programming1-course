"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
"""
The price of a single ride bus ticket in Tampere
and surrounding areas on Aug 23rd, 2020.

The rules used by the program are:

  -----  -------
   Age    Price
  -----  -------
   >24     2.04
  17-24    1.47
   7-16    1.02
   0-6     0.00

Limited usefulness, the actual rules are more complex.
"""


def main():

    try:
        age = int(input("Please, enter your age: "))
    except ValueError:
        print("Input was not a number")
        return

    if age < 7:
        ticket_price = 0.00
    elif age < 17:
        ticket_price = 1.02
    elif age < 25:
        ticket_price = 1.47
    else:
        ticket_price = 2.04

    print("Your ride will cost:", ticket_price)


if __name__ == "__main__":
    main()