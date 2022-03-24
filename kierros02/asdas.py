
"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
def number_input_manager(string, float_or_int):
    """
    Asks input from user with changeable question and checks if input is an positive int.

    :Param string: str, question asked inside input function
    :Return: int, user input if it was an int
    """

    while True:
        answer = input(string)
        try:
            answer = float_or_int(answer)

            if answer >= 0:  # if positive
                return answer  # input was an positive int so we return it
                # break

            else:
                print("Input can not be negative")

        except ValueError:
            print("Bad input")  # input wasn't an int

FIRST_FRIDAY = 3

def main():

    day_count = 7 - FIRST_FRIDAY

    for month in range(1, 13):

        if month in (1, 3, 5, 7, 8, 10, 12):
            amount_of_days = 31

        elif month == 2:
            amount_of_days = 28

        else: # month in [4, 6, 9, 11]:
            amount_of_days = 30

        for day in range(1, amount_of_days + 1):
            day_count += 1
            if day_count % 7 == 0:
                print(f"{day}.{month}.")


if __name__ == "__main__":
    main()
